//
//  ContentView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/19/21.
//

import SwiftUI

// HACK to work-around the smart quote issue
extension NSTextView {
    open override var frame: CGRect {
        didSet {
            self.isAutomaticQuoteSubstitutionEnabled = false
        }
    }
}

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
            .onAppear {
                pythonScript.load()
                pythonScript.run(clear: settings.shouldClear)
            }
            if let image = pythonScript.image {
                VStack {
                    Image(nsImage: image)
                        .resizable().aspectRatio (contentMode:.fit)
                    HStack {
                        Button {
                            let pb = NSPasteboard.general
                            pb.clearContents()
                            pb.writeObjects([image])
                        } label: {
                            Text("Copy")
                        }.disabled(pythonScript.image == nil)

                    }
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ScriptView(name: "sample")
    }
}
