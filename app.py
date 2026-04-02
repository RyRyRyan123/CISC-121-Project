import gradio as gr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def process_input(user_input):
    try:
        string_list = user_input.split(",")
        int_list = [int(x.strip()) for x in string_list]

        sorted_list = quick_sort(int_list)

        return str(sorted_list)
    except ValueError:
        return "Error: Please enter only numbers separated by commas."


test_string = "34, 7, 23, 32, 5, 62"
print("Input:", test_string)
print("Output:", process_input(test_string))

with gr.Blocks(theme=gr.themes.Soft(), title="Quick Sort Visualizer") as demo: 
    gr.Markdown("### Quick Sort Algorithm\nEnter a comma-separated list of numbers to sort them instantly!") 
    
       list_input = gr.Textbox(label="Enter unsorted numbers", placeholder="e.g., 34, 7, 23, 32, 5")
    
       output_display = gr.Textbox(label="Sorted Result") 
    
      sort_btn = gr.Button("Run Quick Sort") 
    
       sort_btn.click(fn=process_input, inputs=list_input, outputs=output_display) 

demo.launch() 
