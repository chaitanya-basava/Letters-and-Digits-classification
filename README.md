# Letters-and-Digits-classification

In this repository we can find three ipynb files, each file contains the code for the following:
<ol>
  <li>The <b>OFL_Assign_1.ipynb</b> file contains the code for a basic binary classifier, which classifies if the input image contains a letter or a digit.</li>
  <li>The <b>OFL_Assign_2.ipynb</b> file contains the code for a four class classifier, the four classes are even, odd, vowel and consonant. The classifier has to predicit what type does the input image contain in an end-to-end fashion.</li>
  <li>The <b>OFL_Assign_3.ipynb</b> file contains a classifier to classify what letter or digit is present in the input image.</li>
</ol>

The dataset used for training these classifiers is <b>emnist</b> dataset which contains 47 classes (10 - digits, 26 - lower case letters and 11 - upper case letters). In the train set there are a total of 112,800 (2,400 per class) images and in the test set there are 18,800 (400 per class) images. The dataset can be downloaded from <a href="https://drive.google.com/open?id=12OYCKGQp1VybvLM157ioLU4Bjt7PWpt-">Here</a>. Else you can directly download the processed npy files from <a href="https://drive.google.com/drive/folders/1mM0AXR0dk0fFucac0bRi7SrIl90g3KJK?usp=sharing">Here</a> and place them in npy_files directory.

<hr>
The accuracies obtained for each tasks are as follows
<ul>
  <li>
    First task:
    <table>
      <tr><th>Train</th><th>Test</th></tr>
      <tr><td>94.61</td><td>93.53</td></tr>
    </table>
  </li>
  <li>
    Second task:
    <table>
      <tr><th>Train</th><th>Test</th></tr>
      <tr><td>93.63</td><td>92.79</td></tr>
    </table>
  </li>
  <li>
    Third task:
    <table>
      <tr><th>Train</th><th>Test</th></tr>
      <tr><td>92.10</td><td>89.71</td></tr>
    </table>
  </li>
</ul>

The <b>classwise_results_ques3.txt</b> file contains the classwise results (i.e., precision, recall, f1-score for each class) for the 3rd task.
<hr>
The pre-trained models can be loaded from the models directory, where there is a h5py file for each of the 3 tasks.
simply use the following line and replace "model_name" with model that you wish to load<br>
<p style="text-align:center">keras.models.load_model("./models/<b>model_name</b>.h5")</p><br>
  <b>NOTE: </b>No need to write any code for the model this line will directly load the trained mdoel with the pre-trained weights.
<hr>

All the 3 models which were used for each induvidual tasks are fairly similar which contain CNN, BatchNorm, Leaky-ReLU, max-pooling, fully connected and softmax layers. The accuracy results shown in the above tables were obtained by doing hyper parameter tunning to best fit the data.

<hr>

The last cell block in each ipynb files contains the code to see the results by selecting an image manually from the testset to see how the model works. There is still a lots of room to improve each of these models, especially the first and second as the data in those cases is not equally distributed. As the number of images for digits (both upper and lower case included) are more than that of letters.
