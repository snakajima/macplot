//
//  ContentView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import SwiftUI

struct ContentView: View {
    @StateObject var pythonScript = PythonScript()
    var body: some View {
        VStack {
            TextEditor(text: $pythonScript.script)
            Button(action: {
                pythonScript.run()
            }, label: {
                Text("Run")
            })
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
