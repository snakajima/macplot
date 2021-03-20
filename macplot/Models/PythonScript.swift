//
//  PythonScript.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import Foundation
import PythonKit

class PythonScript: ObservableObject {
    let tempURL = URL(fileURLWithPath: NSTemporaryDirectory())
    @Published var script:String = ""
    
    init() {
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
            sample.main("/Users/satoshi/git/mm/macplot/macplot/plot2.png")
        } catch {
            print("error saving file")
        }
    }
}
