from googlesearch import search

def search_medicine_for_disease(disease):
    query = f"{disease} medicine products in amazon, flipkart, bighaat"
    search_results = search(query)

    print(f"Product links for {disease}:")
    count = 0
    links = []
    for result in search_results:
        if "amazon.in" in result or "flipkart.com" in result or "bighaat.com" in result:
            count += 1
            #print(f"{count}. {result}")
            links.append(result)
            if count == 5:  # Stop after printing 5 results
                break
    return links

if __name__ == "__main__":
    disease = input("Enter the name of the disease: ")
    links = search_medicine_for_disease(disease)
    print(f"{links=}")
