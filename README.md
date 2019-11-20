# Tapsearch

Tap Search is a web app in which you give search for word and it list out top 10 paragraohs in which the word is present according to the frequency of the word.

## How to use Tapsearch

Tap Search has 3 functionalities:

#### Clear

Through this funcitonality user can clear the database

#### Index

This functionality will allow user to put text in it, and convert the input to inverted index then store it to the database.

#### Search

This functionality will allow the user to input a word/words, and will display the top 10 paragraph/documentID sorted in descending order of the frequency count of a particular word in a particular paragraph.    

#### Future Scope

###### Removing of Stop Words: 
Stop words are most occuring and useless words in document like “I”, “the”, “we”, “is”, “an”.
###### Stemming of Root Word:
Whenever I want to search for “cat”, I want to see a document that has information about it. But the word present in the document is called “cats” or “catty” instead of “cat”. To relate the both words, I’ll chop some part of each and every word I read so that I could get the “root word”. There are standard tools for performing this like “Porter’s Stemmer”.

## Sample Input 

#### Input document

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in elit malesuada, aliquet mauris a, consectetur lorem. Curabitur interdum sit amet tortor sed laoreet. Fusce ac est nulla. Donec id elementum ipsum, ac mollis enim. Fusce id tincidunt lectus. Integer vel purus neque. Donec erat diam, pharetra quis nulla vitae, molestie commodo velit. Duis quis nunc aliquet, laoreet quam eu, ultricies libero. In convallis ullamcorper mi sed viverra. Nunc faucibus tristique magna. Ut et dignissim mauris. Proin lacinia lectus iaculis lorem consequat, quis imperdiet metus cursus. Vivamus sed scelerisque sapien. Curabitur elementum, risus eu faucibus ultrices, massa ligula viverra urna, in faucibus dui metus eget odio. Nullam eget tempus ante. Morbi enim lectus, faucibus vitae nibh et, egestas feugiat lorem.

Pellentesque ut ipsum et dui porta consequat quis quis risus. Vestibulum blandit ultrices quam sed posuere. Curabitur ornare eleifend diam a efficitur. Integer interdum eu urna at scelerisque. Proin sagittis neque a dapibus suscipit. In dignissim feugiat nisl quis blandit. Duis convallis ligula semper est ultricies, non fringilla neque rutrum. Mauris sodales imperdiet posuere. Pellentesque dapibus neque tortor, elementum eleifend erat condimentum sit amet. Proin accumsan ex vel feugiat tincidunt.

Integer sit amet venenatis magna. Integer vulputate egestas nulla quis rutrum. Ut malesuada venenatis elit non laoreet. Proin in lorem non lacus malesuada fermentum. Phasellus nec nisl ornare, sodales orci a, porta quam. Pellentesque eu rhoncus magna, et vestibulum arcu. Praesent tempor porttitor vulputate. Vestibulum at tincidunt magna, vitae luctus tortor.

Aenean consectetur rutrum ex, eu vulputate massa viverra vel. Suspendisse felis erat, euismod nec dolor ac, pretium finibus arcu. In hac habitasse platea dictumst. Morbi vitae scelerisque tortor. Nam enim lacus, molestie quis lobortis sit amet, mattis sed quam. Nam euismod elit a nisl gravida, eu congue ante sollicitudin. Donec ultrices porttitor aliquet. Donec finibus arcu erat, vitae mollis enim scelerisque sagittis. Vivamus lobortis elementum risus, id volutpat eros cursus ac. Duis sem dolor, pulvinar et volutpat ac, tincidunt non lectus. Suspendisse eleifend eros vel mattis maximus. Phasellus lacinia bibendum lectus, quis tristique lacus eleifend vel. Donec fermentum ultrices feugiat. Suspendisse convallis mauris risus, vel mattis turpis tempus sed.

#### Input Queries

1. lorem
2. ipsum
3. et
4. lorem ipsum

## Sample Output

1. For query "lorem" 

lorem = Document Id : 0, Frequency : 4

lorem = Document Id : 2, Frequency : 1

2. For query "ipsum"

ipsum = Document Id : 0, Frequency : 2

ipsum = Document Id : 1, Frequency : 1

3. For query "et"

et = Document Id : 0, Frequency : 2

et = Document Id : 1, Frequency : 1

et = Document Id : 2, Frequency : 1

et = Document Id : 3, Frequency : 1

4. For query "lorem ipsum

lorem = Document Id : 0, Frequency : 4

lorem = Document Id : 2, Frequency : 1

ipsum = Document Id : 0, Frequency : 2

ipsum = Document Id : 1, Frequency : 1

5.For query "lorem ipsum donec"

lorem = Document Id : 0, Frequency : 4

lorem = Document Id : 2, Frequency : 1

ipsum = Document Id : 0, Frequency : 2

ipsum = Document Id : 1, Frequency : 1

donec = Document Id : 3, Frequency : 3

donec = Document Id : 0, Frequency : 2

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
