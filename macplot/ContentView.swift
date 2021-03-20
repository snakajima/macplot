//
//  ContentView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/20/21.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var settings: Settings
    var body: some View {
        NavigationView {
            List {
                NavigationLink("Sample 1", destination: ScriptView(name: "sample"))
                NavigationLink("Sample 2", destination: ScriptView(name: "sample2"))
            }
        }
        .environmentObject(settings)
    }
}

