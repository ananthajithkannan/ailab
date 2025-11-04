import pandas as pd

def calculate_correlation_covariance(file_path):
    
    df = pd.read_csv(file_path)


    numeric_df = df.select_dtypes(include='number')


    correlation_matrix = numeric_df.corr()
    covariance_matrix = numeric_df.cov()

    return correlation_matrix, covariance_matrix

if __name__ == "__main__":
    corr, cov = calculate_correlation_covariance("dataset.csv")

    print("Correlation Matrix:")
    print(corr)

    print("\nCovariance Matrix:")
    print(cov)