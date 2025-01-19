from connectDB import get_data_from_db_1_table_movies, get_data_from_db_2_table_movies, get_data_from_db_2_table_reviews
import pandas as pd
from compare import compare

def mergeData():
    query = "Select * from movies LIMIT 3000"

    listDetailMovies = get_data_from_db_1_table_movies(query)
    listMapIdMovies = get_data_from_db_2_table_movies(query)

    listInfoMovie = []

    # Duyệt qua từng bản ghi trong listDetailMovies
    for recordDetail in listDetailMovies:
        idDetail = recordDetail['name'] 

        for recordMapId in listMapIdMovies:
            movieMapId = recordMapId['originaltitle']  
            if compare(idDetail, movieMapId) > 0.99:  
                
                combined_record = {**recordDetail, **recordMapId}  
                listInfoMovie.append(combined_record)

    # In kết quả kết hợp
    df_listInfoMovie = pd.DataFrame(listInfoMovie)

    # df = df.drop(['endyear'], axis=1)
    # transData(df_listInfoMovie)
    print(df_listInfoMovie)
    getData(df_listInfoMovie)
    
# def transData(df_listInfoMovie):
    
#     tmp = df_listInfoMovie.isnull().all()
    
#     print(tmp)
    
def getData(df_listInfoMovie):
    
    query = "Select * from movie_reviews LIMIT 20000"
    
    listReviewMovie =get_data_from_db_2_table_reviews(query)
    
    df_listReviewMovie = pd.DataFrame(listReviewMovie)

    tconst_list = df_listInfoMovie['tconst'].tolist()
    
    combined_data = []

    for tconst in tconst_list:
        record_listInfoMovie = df_listInfoMovie[df_listInfoMovie['tconst'] == tconst].to_dict('records')[0]
        # print(listReviewMovie)
        records_listReviewMovie = df_listReviewMovie[df_listReviewMovie[1] == tconst].to_dict('records')
        
        if records_listReviewMovie:
            
            total_text = []
            total_summary = []
            sum = 0
            
            for record_listReviewMovie in records_listReviewMovie:
                total_text.append(record_listReviewMovie[4])
                total_summary.append(record_listReviewMovie[6])
                sum += record_listReviewMovie[5]

            count_new_record = len(records_listReviewMovie)
            total_record = record_listInfoMovie['vote_count'] + count_new_record
            
            total_rate = record_listInfoMovie['vote_average'] * record_listInfoMovie['vote_count'] + count_new_record * sum
            vote_average = total_rate / total_record
    
            record_tmp = record_listInfoMovie.copy()
            
            record_tmp['vote_average'] = vote_average
            record_tmp['vote_count'] = total_record
            
            # Tạo bản ghi mới
            record_update = {
                **record_tmp,  # Dữ liệu từ listInfoMovie
                'review_texts': total_text,  # Danh sách review_text
                'review_summaries': total_summary,  # Danh sách review_summary
            }
            combined_data.append(record_update)  # Thêm bản ghi mới vào danh sách
        else:
            # Nếu không có bản ghi tương ứng trong listReviewMovie, giữ nguyên dữ liệu từ listInfoMovie
            combined_data.append(record_listInfoMovie)
        
    # Tạo DataFrame từ dữ liệu kết hợp
    df_combined = pd.DataFrame(combined_data)

    # Hiển thị kết quả
    print(df_combined)
              
  
mergeData()
    
    