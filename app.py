def interface(file, question):
    return chat_with_doc(file, question)


def report_ui(file):
    return generate_report(file)


with gr.Blocks() as app:

    gr.Markdown("# 🔥 InsightPilot AI - Decision Copilot")

    with gr.Tab("Chat with Document"):
        file_input = gr.File()
        question = gr.Textbox(label="Ask Question")
        output = gr.Textbox()

        btn = gr.Button("Ask AI")
        btn.click(interface, inputs=[file_input, question], outputs=output)

    with gr.Tab("Generate Report"):
        file_input2 = gr.File()
        output2 = gr.Textbox()

        btn2 = gr.Button("Generate Report")
        btn2.click(report_ui, inputs=file_input2, outputs=output2)

app.launch()
