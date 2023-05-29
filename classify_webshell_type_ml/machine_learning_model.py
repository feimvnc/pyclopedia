'''
A very simple program to:
-tokenize datasets
-build cassification using tokens
-calculate max p-values from input against cclassification using simple formula
-predict input string for classification

# run program 
python machine_learning_model.py 

Test Sample ..
Debug for try_classify :  ['<?php', 'eval', '$', 'exp', '?>']
>> <?php eval($_GET["exp"]); ?> shell-php-include 0.6666666666666666
Shell Type : shell-php-include 

'''

import os
import sys


class shell_detect :
    
    @staticmethod
    def read_file(file_path) :
        # data = None
        with open(file_path) as f:
            data = f.read()
        return data


    @staticmethod
    def code_word_to_vector(php_code) :
        # list of ignored tokens, just like stop words
        filter_flag_list = ['@','[',']','(',')','{','}','\'','"',',',';','=','.','\t','\n','\r\n']
        # keywords extractions
        tokens = ['$_GET','$_POST','$_REQUEST','$_COOKIE']

        # replace stop words with space 
        for filter_flag_index in filter_flag_list :
            php_code = php_code.replace(filter_flag_index,' ')

        vector = php_code.split(' ')

        # clean up data, or pre-process data 
        for index in range(len(vector)) :  
            if vector[index].startswith('$') and not vector[index] in tokens :
                vector[index] = ''
            elif vector[index] in tokens :
                vector[index] = '$'

        # remove empty item 
        while vector.count('') : 
            vector.remove('')

        return vector


    # read data files from 'datasets' folder
    @staticmethod
    def load_and_train_model(data_set_path = 'datasets') :
        file_list = os.listdir(data_set_path)
        # to store classification
        category = {}          

        for file_index in file_list :
            try :
                file_information = file_index.split('-')
                # file names include labels of data categories
                classfy_type = file_information[0] + '-' + file_information[1] + '-' + file_information[2]
                # create vector of takens from file 
                code_vector = shell_detect.code_word_to_vector(shell_detect.read_file(data_set_path + '/' + file_index))

                # add classification to dict
                if not category.get(classfy_type) :
                    category[classfy_type] = []

                category[classfy_type] = code_vector
                # print(shell_sample)
            except :
                print('Error Shell Sample File !' , file_index)
                print('Sample File Name Format :')
                print('normal-%shell_language%-%shell_type%-%shell_index%.php or ')
                print('shell-%shell_language%-%shell_type%-%shell_index%.php ')

        return category
    

    def __init__(self,data_set_path = 'datasets') :
        self.category = shell_detect.load_and_train_model(data_set_path)
    

    # classify input_code based shell_sample built
    def try_classify(self, input_code) :
        input_code_vector = shell_detect.code_word_to_vector(input_code)
        # constant, or weight
        alpha = 1   
        # to track max values 
        p_list = {}

        print( 'Debug for try_classify : ' ,input_code_vector)

        for key_index in self.category.keys() :
            max_p_value = 0

            for category_index in self.category[key_index]:
                found_vector_in_category_count = 0

                # build token counts
                for token_vector_index in input_code_vector :
                    if token_vector_index in category_index :
                        found_vector_in_category_count += category_index.count(token_vector_index)

                # calculate a math p_value, this is simple formula, 
                p_value = (found_vector_in_category_count + alpha) / float(len(category_index) * 2 + alpha)

                #print( categoryv_index , p_value
                if p_value >= max_p_value :
                    max_p_value = p_value

            p_list[key_index] = max_p_value

            #print( key_index ,p_list[key_index]

        max_p_value = 0
        max_p_type_name = ''

        # loop through p_list, find the max value, and corresponding label 
        for p_type_name_index in p_list.keys() :
            p_value = p_list[p_type_name_index]

            if p_value >= max_p_value :
                max_p_value = p_value
                max_p_type_name = p_type_name_index

        print( ">>", input_code , max_p_type_name , max_p_value)

        return max_p_type_name

    
if __name__ == '__main__' :
    # create an instance, this initiate data loading, and create classification model using pre-provided files 
    model = shell_detect()
    
    if 2 == len(sys.argv) :
        # detect single file content
        print( 'Shell Type :' , model.try_classify(shell_detect.read_file(sys.argv[1])))
    else :
        # classify based on runtime input string
        print( '\nTest Sample ..')
        print( 'Shell Type :' , model.try_classify('<?php eval($_GET["exp"]); ?>'), '\n')
        print( 'Shell Type :' , model.try_classify('<?php assert($_GET["exp"]); ?>'), '\n')
        print( 'Shell Type :' , model.try_classify('<?php system($_GET["exp"]); ?>'), '\n')
        print( 'Shell Type :' , model.try_classify('<?php systen("ifconfig"); ?>'), '\n')
        print( 'Shell Type :' , model.try_classify('<?php echo "123"; ?>'),'\n''\n')
        print( 'Shell Type :' , model.try_classify('<?php $b=1+1; ?>'))
        print( 'Shell Type :' , model.try_classify('<?php phpinfo(); ?>'))
        print( 'Shell Type :' , model.try_classify('<?php $a=create_function(\'\',\'ev\',\'al\'.\'($\'.\'_GET["e"]);\'); $a(); ?>'))
        print( 'Shell Type :' , model.try_classify('<?php include($_COOKIE[\'s\']); ?>'))
        print( 'Shell Type :' , model.try_classify('<?php require_once($_POST[\'s\']); ?>'))
