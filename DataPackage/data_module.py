key_main_table = "main_table" #Clé de la table Principale
key_main_data_frame= "main_data_frame" # Clé de la data frame principale dans dictionnaire mainGlobleData
key_main_column_head_list = "main_column_list"
key_main_column_dtype_dict = "main_column_dtype_dict"
key_main_variable_type = "main_variable_type"

#Les types de variables
var_qt = "Variable Quantitative"
var_ql = "Variable Qualitative"
var_ord = "Variable Ordinale"
var_binaire = "Variable Binaire"
var_temp = "Variable Temporaire"
variableTypeList = [var_qt, var_ql, var_ord, var_binaire, var_temp]





dictGlobalData: dict = {
                        key_main_data_frame : None,
                        key_main_column_head_list : [],
                        key_main_column_dtype_dict : {},
                        key_main_variable_type : {}
                        

}


n_nbr = 4 #Nombre de chiffre après la virgule