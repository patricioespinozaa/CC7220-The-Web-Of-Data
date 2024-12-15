# STREAMFUSION RDF

## Project Description

This project was developed as part of the **CC7220 - The Web of Data** course at the **Faculty of Physical and Mathematical Sciences, University of Chile**.

The primary objective was to explore the availability of movies and series across various streaming platforms, such as **Amazon**, **Netflix**, and **HBO Max**. The project involved combining two or more datasets containing information about the content available on these platforms.

Using this data, the project aims to provide users with insightful queries, such as:

1. **Names and number of platforms on which a movie is available**  
   Retrieves the number of streaming platforms (e.g., Amazon, Netflix, HBO Max) where a specific movie is available.

2. **Movies that are available on the same platform but vary by country**  
   Identifies movies available on the same platform whose availability differs by country due to geographic restrictions, dubbing, or other factors.

3. **Dominant genre on each platform**  
   Determines the predominant genre on a specific platform based on the number of movies or series available in that genre.

4. **Popular genres in Chile**  
   Analyzes the most popular genres of movies and series in Chile according to the streaming platforms available in the country.

5. **Number of movies available by country**  
   Counts the total number of movies available in each country, reflecting regional differences in content availability.

6. **Number of movies available by platform**  
   Provides a count of how many movies are available on each streaming platform, such as Netflix, Amazon, and HBO Max.

7. **Number of movies released by decade**  
   Analyzes how many movies were released by decade, offering insights into trends and the evolution of the film industry over time.

The primary focus was to offer an enriched way to query content availability and trends across streaming platforms.

---

## Replication

To replicate this project, follow these steps:

1. **Download the datasets**  
   Obtain the datasets listed in the [References](#references) section.

2. **Unify the data**  
   Run the `clean.py` script to combine the information into a single CSV file.

3. **Transform the data into RDF triples**  
   Use **RMLMapper** to convert the CSV file into RDF triples:
   - Run the following command in the terminal:
     ```bash
     java -jar rmlmapper.jar -m query_data.ttl -o results.ttl
     ```
   - This command will generate a `results.ttl` file in RDF Turtle format.

4. **Upload the data to Apache Jena Fuseki**  
   Load the `results.ttl` file into **Apache Jena Fuseki**.  
   Once uploaded, you can perform SPARQL queries on the data.

5. **Query the data**  
   The queries developed by the team are available in the `All_Queries.ttl` file.

This process transforms and loads the data for analysis using Apache Jena Fuseki.

---

## Team

- Rodrigo Araya
- Patricio Espinoza
- Matías Rivera

---

## References

- [Full Amazon Prime Dataset](https://www.kaggle.com/datasets/octopusteam/full-amazon-prime-dataset)
- [Full HBO Max Dataset](https://www.kaggle.com/datasets/octopusteam/full-hbo-max-dataset)
- [Full Netflix Dataset](https://www.kaggle.com/datasets/octopusteam/full-netflix-dataset)
- [RDF Mapping Language (RML)](https://rml.io/specs/rml/)
- [Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/)