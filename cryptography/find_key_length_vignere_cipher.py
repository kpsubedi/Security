#!/usr/bin/python
# 

def count_match_in_string(str1, str2):
    count = 0
    for i in range(len(str2)):
        if str1[i]==str2[i]:
            count = count + 1
    return count

def main():
    input_list = []
    input_str="kphflxfvobrvzvqhoaymqlewredotgvqwozsbmgjzsuvdwfvvlvkpxywxjsxjblowmkpdggiigorykttdzdeeldjcirbpdyckmhwswfakhqicbwklxzbrxrlkbrepximdwphnqwkcijxhfegymvktvvxvdwymehreezdwsiiblpthcgdvdlvllgyskiwdwpbvrzhlvbkhcmkerxwhcqnhelvvdpplfehypvzbrqwcxzlqyiuiolexcmzloiikrppmkasopejmgvzjrzwkzyxpwdwmtmdqowymzhyxfvzrfpugrxeictphapvivhhlzkkzlczwxjsxkwjrqvfukhcikpdwoigmqgdexwrgoirtrqhlvzhbzyniqwesxmwwzwrqgwsitiwlosebpxnltiuhhlvzhvlmuiolnikphqtxuwhvyxdiwwpvnplfsargbrfkfadloxymfdewftrqrejqjhewfuhzsiimdotgviggphradqpbgtdqlxzwqrscfcuhdyimwroskpdwdezlwkpgrblijslwqojartnozrxmqrfkyiolniwmowelrbwktwtwxoorfbehoieqhgdsjphwcmvldqzxymutfijblryayiwvzvkwispsgthotzvierfxymuhtrkpdwomimfwtsebkhnekadloardlqrmkaulrlkxdzcslvgotzvadklxkmudyhzvwklxuquhnxzwqzlzzvjwsifbkhctreolgijipdcgypdupzzalwpmkphujsltlnpxymbupffbkplhscwlosebzdyxkwjrlqfvjplhgmrswirtlfpvvuduviuwkbzytiqwsicxwklxjilgelvkdwhiimdowqrlkhcizupdocfcuhxeuprzospwxnysnqpplhjilglpzkhbzydcvwmijilgelvkdwzvpwxzzyclqwsemmfrxiymuhdlrlrzmeesfkpwyquh"
    for i in range(1,901):
        input_list.append(input_str[i:len(input_str)])
    print len(input_str)
    occurrence_list = []    
    for i in range(len(input_list)):
        c = count_match_in_string(input_str, input_list[i])
        occurrence_list.append(c)
    print occurrence_list, len(occurrence_list)        

if __name__=='__main__':
    main()

