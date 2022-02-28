## Get Started
To start AUTOflow, the AUTOflow.py file is executed.</br>
Afterwards, the first window of the GUI will be opened. The tool consists of two parts. Therefore, in the first window, you can choose which part of the AUTOflow tool you want to use. You can train a new model from scratch, by using AutoKeras, according to a database of you. The other option is to use an already trained model, optimize and convert it into a format to execute it on your target platform. If you want, you can also first train a new model from scratch and optimize and convert it afterwards for your target platform.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_1.PNG" width="45%" height="45%">
</p>

### Train model from scratch
If you want to train a new model from scratch (left button) you will see this window next. Here the model name, the output path and the data to train the neural network are passed.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_2.PNG" width="45%" height="45%">
</p>


In the next window, the task to be solved by the neural network can be selected. Four different tasks are available for selection: Image classification, Image regression, Data classification and Data regression.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_3.PNG" width="45%" height="45%">
</p>


Next, some parameters have to be passed to AutoKeras for automatic model generation. These are:
- The number of epochs each model should be trained.
- The number of different models that should be trained.
- The maximum size of the models. (If this parameter is 0, there is no limit to the size of the model).

If the data is passed in the form of images, the height and width of the images (number of pixels), as well as the number of color channels, have to be passed additionally. If everything is passed, the automatic model generation can be started.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_4.PNG" width="45%" height="45%">
</p>


In the last window of this part of the AUTOflow tool you have to wait until the automatic model generation is finished. Then you will be returned to the GUI start window.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_train_5.PNG" width="45%" height="45%">
</p>



### Load trained model
If you want to use an already trained model (right button) you will see this window next. Here the project name, the output path and the neural network to be converted are passed.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_2.PNG" width="45%" height="45%">
</p>


In the next window you can select the target you want to execute the TensorFlow model. You can choose if you want to execute it on a microcontroller, a FPGA or an embedded PC.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_3.PNG" width="45%" height="45%">
</p>


In the fourth window, the optimization algorithms pruning and quantization can be selected. It is important to know that only for fully connected and convolutional layers the pruning algorithm can be applied.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_4.PNG" width="45%" height="45%">
</p>

If you select pruning, you can choose between two options:
- Factor: For the fully connected and convolutional layers, a factor is specified in each case, which indicates the percentage of neurons or filters to be deleted from the layer.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_4a.PNG" width="45%" height="45%">
</p>

- Accuracy: The minimum accuracy of the neural network or the loss of accuracy that may result from pruning can be specified here.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_4b.PNG" width="45%" height="45%">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_4c.PNG" width="45%" height="45%">
</p>

If quantization is selected, you can choose between two options:
- int8 + float32: This quantization approach converts all weights to int8 values. But the input and output still remain 32-bit float.
- int8 only: All weights get converted to int8 values. Also the input and output will be converted to 8-bit integer. When executing the net later, the input values of the model must be passed as signed int8 values. Also the output values are returned as signed int8 values.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_4d.PNG" width="45%" height="45%">
</p>


The next window appears only if at least one optimization algorithm has been selected. In this window the training data are selected which the neural network requires for the optimization. The data can be transferred in different ways:
- Path: Images are to be used as training data. In the given path there are subfolders containing the name of the different classes of the neural network and the corresponding images.
- File (CSV file): The data is stored in a CSV file. An example of how such a file can look like can be found [here](https://github.com/Hahn-Schickard/AUTOflow/blob/main/Example/Input_data/Datenvorverarbeitung_MNIST.py).
- File (Python file): The data is loaded and returned in a Python script. Here it is important that the Python script contains the function get_data() with the return values x_train, y_train, x_test, y_test (training data, training label, test data, test label). The return values here are Numpy arrays.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_5.PNG" width="45%" height="45%">
</p>

If a CSV file is selected the CSV dataloader window opens. With the browse button a new CSV file can be selected again. By using the different separators, it is possible to define how the data is separated. The Preview button shows an overview of how the data will look with the selected settings. In addition, the label of each data series must be specified. Here it is possible to set the label to the first or the last position of a data series. In addition, the number of rows and columns in the data set is displayed. If all settings are correct, the settings can be taken over for the later optimization via the button Load data.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_5a.PNG" width="45%" height="45%">
</p>


At the end, if you want to execute the TensorFlow model on a microcontroller you have to specify the amount of memory for the input, output, and intermediate arrays of the neural network on the microcontroller. If you select another device, you don't have to do that. In addition, an overview of all selected parameters is displayed here. The button in the lower right corner starts the process of the conversion.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_load_6a.PNG" width="45%" height="45%">
</p>


## Model execution
The optimized model which has been converted to the TensorFlow Lite format is stored in the project folder which was specified as the output path. The following shows some code snippets that are needed to execute the TensorFlow Lite model on an embedded PC:
```
# Read the data of your TFLite model file
with open(tflite_model_file, 'rb') as f:
    tflite_model = f.read()
...
# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
...
# Get input and output of model
input = interpreter.get_input_details()[0]
output = interpreter.get_output_details()[0]
...
# Set input data
interpreter.set_tensor(input['index'], input_data)
...
# Run the model
interpreter.invoke()
...
# Get model output
prediction = interpreter.get_tensor(output['index'])
```

Moreover, an example script for executing a TFLite model, trained on the MNIST dataset, can be found [here](https://github.com/Hahn-Schickard/AUTOflow/blob/main/Example/Templates/Embedded_PC_MNIST.py).