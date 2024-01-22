import os
import json
import PyPDF2
import traceback

def read_file(file) :
    if file.name.endswith('pdf') :
        try :
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page in pdf_reader.pages :
                text += page.extract_text()
            return text
        except Exception as e :
            raise Exception("Error in reading PDF file")
    
    elif file.name.endswith('.txt') :
        return file.read()
    else :
        raise Exception('Unsupported file format. only PDF and TEXT files are supported')
    
def get_table_data(quiz_str) :
    try :
        quiz_dic = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dic.items() :
            mcq = value['mcq']
            options = " || ".join(
            [
                f"{option}: {option_value}" for option, option_value in value["options"].items()
            ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    
    except Exception as e :
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    
            

    