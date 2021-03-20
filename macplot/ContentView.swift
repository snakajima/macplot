//
//  ContentView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/20/21.
//

import SwiftUI

struct Sample: Identifiable {
    let id: String
    let title: String
}

let samples = [
    Sample(id: "sample", title: "Decaying Sin Wave"),
    Sample(id: "sample2", title: "Decaying Sin Wave with another Sin Wave"),
    Sample(id: "sample3", title: "Normal Distribution"),
]

struct ContentView: View {
    @EnvironmentObject var settings: Settings
    var body: some View {
        NavigationView {
            List {
                ForEach(samples) {
                    NavigationLink($0.title, destination: ScriptView(name: $0.id))
                }
            }
        }
        .environmentObject(settings)
    }
}

