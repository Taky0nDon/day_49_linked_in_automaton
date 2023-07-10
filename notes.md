`jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")`
finds 24 elements, but only the first 7 have the
a tag loaded. 

## I need to load all the data before scraping.
Has something to do with `::after`

## How to scroll a frame/sidebar in selenium
* move to element
* scroll (send arbitrary pagedowns?)
* Try clicking, letting right frame load (sleep), click
again, then scroll.

## THIS WORKED I THINK:
* move to the last li element in the jobs container element
* sleep for 2 seconds
* then find all the jobs
* STILL ONLY FOUND 11 FUCKIN JOBS (BETTER THAN 7!!!)
* NEED TO SOMEHOW REFRESH THE JOBS EVERY N JOB CLICKS
* if clicked_jobs % 7 == 0: refresh jobs?
* move to element, then scroll 150 down in y worked!! 22 jobs clicked!
