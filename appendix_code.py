import pandas as pd
import matplotlib.pyplot as plt

# Load your data
file_path = r'C:\Users\Bashir\Desktop\Bashir Bioengineering\Model_Results_with_Endpoints.csv'
data = pd.read_csv(file_path)

# Get the unique endpoints
endpoints = data['Endpoint'].unique()

# Create the figure and axes for the subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Loop over each endpoint and plot its respective metrics
for i, endpoint in enumerate(endpoints):
    # Filter data for the current endpoint
    subset = data[data['Endpoint'] == endpoint]
    
    # Set 'Model' as the index and plot precision, sensitivity, and F-measure
    subset.set_index('Model')[['Precision', 'Sensitivity', 'F-measure']].plot(kind='bar', ax=axes[i])
    
    # Set titles and labels for each subplot
    axes[i].set_title(f'Performance Metrics for {endpoint}')
    axes[i].set_ylabel('Score')
    axes[i].legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better visualization
plt.tight_layout()

# Display the plot
plt.show()
