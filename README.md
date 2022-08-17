# qa_python
# test_add_new_book_add_two_books(self)
# This test verifies that add_new_book can add two books

# test_add_new_book_default_rating_result1(self)
# This test verifies that add_new_book addes a book with a default rating = 1

# test_add_new_book_the_same_book_twice_result1(self)
# This test verifies that add_new_book can't add two similar books

# test_set_book_rating_to_5_result5(self)
# This test verifies that set_book_rating sets rating 5 to an existing book

# test_set_book_rating_to_outrange0_result1(self)
# This test verifies that rating 0 can't be set so an existing book keeps a default rating = 1

# test_set_book_rating_to_outrange11_result1(self)
# This test verifies that rating 11 can't be set so an existing book keeps a default rating = 1

# test_set_book_rating_to_nonexisting_book_result_None(self)
# This test verifies that a rating can't be set to not existing book

# test_get_book_rating_for_existing_book_result1(self)
# This test verifies that get_book_rating returns a rating of the book. The default one in this case (=1).

# test_get_book_rating_nonexisting_book_result_None(self)
# This test verifies that get_book_rating returns None for not existing book

# test_get_books_with_specific_rating_2of3books_result2(self)
# This test verifies that get_books_with_specific_rating returns 2 of 3 books with a specified rating, the 3rd book has another rating. 

# test_add_book_in_favorites_add_existing_book_result1(self)
# This test verifies that add_book_in_favorites adds existing book.

# test_add_book_in_favorites_add_nonexisting_book_result0(self)
# This test verifies that a not existing book can't be added to favorites.

# test_add_book_in_favorites_add_the_same_book_twice_result1(self)
# This test verifies that the same book can't be added to favorites.

# test_delete_book_from_favorites_existing_book_result0(self)
# This test verifies that delete_book_from_favorites deletes an existing book from the favorites list.

# test_delete_book_from_favorites_nonexisting_book_result1(self)
# This test verifies that not existing book can't be deleted from favorites. 
