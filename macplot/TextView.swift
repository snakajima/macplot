//
//  TextView.swift
//  macplot
//
//  Created by SATOSHI NAKAJIMA on 3/20/21.
//

import SwiftUI

struct TextView : NSViewRepresentable {
    typealias NSViewType = NSTextView
    @Binding var text:String
    
    func makeCoordinator() -> Coordinator {
        return Coordinator(text: $text)
    }
    
    func makeNSView(context: Context) -> NSTextView {
        let view = NSTextView()
        view.delegate = context.coordinator
        return view
    }
    
    func updateNSView(_ nsView: NSTextView, context: Context) {
        nsView.string = text
    }
    
    class Coordinator: NSObject, NSTextViewDelegate {
        @Binding var text:String
        init(text: Binding<String>) {
            _text = text
        }
        func textDidChange(_ notification: Notification) {
            if let textView = notification.object as? NSTextView {
                text = textView.string
            }
        }
    }

}
