# Wheat_kernel_classifier
This is a wheat kernel classifier web application.

Data Description:
This dataset predicts the type of kernel based on the different indicators as below:
To construct the data, seven geometric parameters of wheat kernels were measured:
1. Area A,
2. Perimeter P,
3. Compactness C = 4*pi*A/P^2,
4. Length of kernel,
5. Width of kernel,
6. Asymmetry coefficient
7. Length of kernel groove.
All of these parameters were real-valued continuous.
Apart from training files, we also require a "schema" file from the client, which contains all the relevant information about the training files such as:
Name of the files, Length of Date value in FileName, Length of Time value in FileName, Number of Columns, Name of the Columns, and their datatype.
