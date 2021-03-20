//
//  PythonScript.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import Foundation
import PythonKit

class PythonScript: ObservableObject {
    @Published var script:String = ""
    
    init() {
        if let url = Bundle.main.url(forResource: "sample", withExtension: "py") {
            script = (try? String(contentsOf: url, encoding: .utf8)) ?? ""
        }
    }
    
    func run() {
        let sys = Python.import("sys")
        sys.path.append("/Users/satoshi/git/mm/macplot/macplot")
        let sample = Python.import("sample")
        sample.main("/Users/satoshi/git/mm/macplot/macplot/plot2.png")
    }
}
