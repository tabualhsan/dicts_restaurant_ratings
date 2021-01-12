"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(filename):

    # open score file
    ratings = open(filename)

    # create empty dictionary
    ratings_review = {}

    # read ratings in file, split lines:
    for rating in ratings:
        sentences = rating.rstrip()

        full_restaurant_lst = sentences.split(":")
        print(full_restaurant_lst)
        key = full_restaurant_lst[0]
        value = full_restaurant_lst[1]
        # for restaurant, score in full_restaurant_lst:
        
        ratings_review[key] = value
    # put items into dictionary
        # for restaurant, score in full_restaurant_lst.items():
            # ratings_review[restaurant] = ratings_review.get(restaurant)
           
           
           
    # convert number string into integer

    
    
    # ratings_review[full_restaurant_list[::2]] = full_restaurant_list[1::2]
    # restaurants == full_restaurant_list[::2]
    # ratings == full_restaurant_list[1::2]


    #sort the items
        print (ratings_review)
    return ratings_review
       
    #         print (f'{restaurant} {score}')
    # return f'{restaurant} {score}'

        




# put ratings in alphabetical order by restaurant
# print f-string "restaurant is rated, score"

restaurant_ratings('scores.txt')
