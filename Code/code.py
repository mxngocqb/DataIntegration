from connectDB import get_data_from_db_1_table_movies, get_data_from_db_2_table_movies
import pandas as pd
from compare import compare

query = "Select * from movies LIMIT 1000"

row1 = get_data_from_db_1_table_movies(query)
row2 = get_data_from_db_2_table_movies(query)

row3 = []

# Duyệt qua từng bản ghi trong row1
for record1 in row1:
    id1 = record1['name'] 

    for record2 in row2:
        movieId2 = record2['originaltitle']  
        if compare(id1, movieId2) > 0.99:  
            
            combined_record = {**record1, **record2}  
            row3.append(combined_record)

# In kết quả kết hợp
df = pd.DataFrame(row3)

# df = df.drop(['endyear'])

# Hiển thị bảng
print(df)