//
//  ContentView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import SwiftUI

struct ScriptView: View {
    @StateObject var pythonScript: PythonScript
    @EnvironmentObject var settings: Settings
    
    init(name: String) {
        let script = PythonScript(name: name)
        _pythonScript = StateObject(wrappedValue: script)
    }
    var body: some View {
        HStack {
            VStack {
                TextEditor(text: $pythonScript.script)
                HStack {
                    Button(action: {
                        pythonScript.run(clear: settings.shouldClear)
                    }, label: {
                        Text("Plot")
                    })
                    Toggle("Clear", isOn: $settings.shouldClear)
                }
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
        ScriptView(name: "sample")
    }
}
