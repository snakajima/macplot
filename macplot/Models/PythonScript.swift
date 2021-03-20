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
    let imageURL = URL(fileURLWithPath: "/Users/satoshi/git/mm/macplot/macplot/plot2.png")
    @Published var script: String = ""
    @Published var image: NSImage?
    
    init() {
        //imageURL = tempURL.appendingPathComponent("plot.png")
        if let url = Bundle.main.url(forResource: "sample", withExtension: "py") {
            script = (try? String(contentsOf: url, encoding: .utf8)) ?? ""
        }
    }
    
    func run() {
        let sys = Python.import("sys")
        let filename = UUID().uuidString
        let url = tempURL.appendingPathComponent("\(filename).py")
        do {
            try script.write(to: url, atomically: true, encoding: .utf8)
            sys.path.append(tempURL.path)
            let sample = Python.import(filename)
            sample.main(imageURL.path)
            image = NSImage(contentsOfFile: imageURL.path)
        } catch {
            print("error saving file")
        }
    }
}
