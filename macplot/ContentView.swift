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
    Sample(id: "circle", title: "Circle"),
    Sample(id: "flower", title: "Flower"),
    Sample(id: "piechart", title: "Pie Chart"),
    Sample(id: "salaries", title: "Median Salary (USD) by Age"),
    Sample(id: "stock", title: "Historical Stock Price: TSLA"),
    Sample(id: "poisson", title: "Poisson Distribution"),
    Sample(id: "b-spline", title: "B-Spline"),
    Sample(id: "julia", title: "Julia Fractal"), // NOTE: Does not look good
    Sample(id: "mandelbrot", title: "Mandelbrot Fractal"), 
    Sample(id: "random", title: "Random Walk"),
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

