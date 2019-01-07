# Marvel-universe-python
The second project of my class on the features and structure of languages. We were instructed to use the language python to analyze the structure of the marvel comics universe based on a research paper. This assignment is extremely similar to an assignment for my algorithms class which you can find in the repository “Marvel-universe-as-a-social-network-java”. Both were assigned by the same professor in different classes.

You can see the assignment as “CSCI 3415 - Program 2.pdf”, and my final report as “report.docx”. The following is adapted from my final report.

## Assignment
We were asked to build a python program to analyze data about the marvel comics universe. I used python 3 installed via anaconda.

## Methodology
My methodology was to read in the list of comics and characters as 1D arrays than generate 2D arrays that contained the data on collaboration. I then used the 2D arrays to generate the data to be analyzed. For testing purposes the a function called outputTest was written. It writes the content of a 2D array to a csv (these csv files were huge).

### Reading
Each read block is essentially the same. They specify a descriptive variable name for each entry in a row and use an if statement to insert the data into its proper location. When reading in nodes.csv a 0 is placed at the beginning of each list so that later 2D arrays have no overlapping names. Hero-network.csv contains a number of special case typos that had to be dealt with upon reading the file. Some were simply edited out of the data.

### 2D Array processing
The 2 2D arrays are an array of all character crossovers called collabArray and an array of all character appearances in a book called inBookArray. In each a 1 was inserted for entries in edges.csv and hero-network.csv respectively. Outputting these arrays created the largest spreadsheets I’ve ever seen. Excel had trouble loading them but I managed to color each 1 in red and screenshot dense areas in them (These images are horizontally squished because I use an 21/9 monitor and can be found in the report.docx file)

### Solving for the desired values
To solve for the assigned values I simply summed the relevant data from the 2D arrays. For the number of characters per book a made a 1D array and summoned the coulmbs of inBookArray. For the number of appearances for a character I summed the rows and for the number of collaborations I could have done either dimension in collabArray ( I did the coulmbs for the record). I then sorted these 1D arrays (which was super slow I want to look into the Array.sort() function) to find min and max. I then found the mean for these things. Here are my sample results



     reading nodes.csv
     
     reading edges.csv
     
     reading hero-network.csv
     
     The number of comics is: 12652
     
     The number of characters is: 6440
     
     The min, mean, and max number of characters per book are :1, 7.596553632123943, and 111
     
     The min, mean, and max number of book appearances per character are :1, 14.925298959465756, and 1577
     
     The min, mean, and max number of collaborators per character are :0, 34.80524926230781, and 1428`
