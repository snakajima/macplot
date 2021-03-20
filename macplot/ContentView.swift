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
        HStack {
            VStack {
                TextEditor(text: $pythonScript.script)
                Button(action: {
                    pythonScript.run()
                }, label: {
                    Text("Plot")
                })
                if let errorMsg = pythonScript.errorMsg {
                    Text(errorMsg)
                        .foregroundColor(.pink)
                }
            }
            if let image = pythonScript.image {
                Image(nsImage: image)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
