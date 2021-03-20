//
//  macplotApp.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import SwiftUI

@main
struct macplotApp: App {
    var body: some Scene {
        WindowGroup {
            NavigationView {
                List {
                    NavigationLink("Sample 1", destination: ScriptView(name: "sample"))
                    NavigationLink("Sample 2", destination: ScriptView(name: "sample2"))
                }
            }
        }
    }
}
