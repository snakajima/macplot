//
//  PythonScript.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import Foundation
import PythonKit
import AppKit

class PythonScript: ObservableObject {
    let tempURL = URL(fileURLWithPath: NSTemporaryDirectory())
    let imageURL: URL
    let clear: PythonObject
    let savefig: PythonObject
    @Published var script: String = ""
    @Published var errorMsg: String? = nil
    @Published var image: NSImage? = nil
    @Published var shouldClear: Bool = true
    
    init() {
        imageURL = tempURL.appendingPathComponent("plot.png")
        if let url = Bundle.main.url(forResource: "sample", withExtension: "py") {
            script = (try? String(contentsOf: url, encoding: .utf8)) ?? ""
        }
        clear = Self.load("clear")!
        savefig = Self.load("savefig")!
    }
    
    static func load(_ name: String) -> PythonObject? {
        guard let url = Bundle.main.url(forResource: name, withExtension: "py") else {
            return nil
        }
        var components = url.pathComponents
        components.removeLast()
        let path = components.joined(separator: "/")
        let sys = Python.import("sys")
        sys.path.append(path)
        return Python.import(name)
    }
    
    func run() {
        let sys = Python.import("sys")
        let filename = UUID().uuidString
        let url = tempURL.appendingPathComponent("\(filename).py")
        do {
            if shouldClear {
                clear.main()
            }
            try script.write(to: url, atomically: true, encoding: .utf8)
            sys.path.append(tempURL.path)
            let sample = try Python.attemptImport(filename)
            try sample.main.throwing.dynamicallyCall(withArguments: [])
            savefig.main(imageURL.path)
            image = NSImage(contentsOfFile: imageURL.path)
            errorMsg = nil
        } catch {
            if let pyError = error as? PythonError {
                errorMsg = pyError.description
            }
        }
    }
}
