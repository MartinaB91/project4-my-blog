# Test and validations

## Table of contents
- [Introduction ](#introduction)
- [Test](#test)
    - [Test cases](#test-cases)
    - [Responsiveness tests](#responsiveness-tests)
    - [Exploratory tests](#exploratory-tests)
    - [Usability testing](#usability-testing)
    - [Automatic tests](#automatic-tests)
    - [Lighthouse reports](#lighthouse-reports)
- [Validation](#validation)

## Introduction 
During the development process, unit testing has been done to check if functionality is as expected. Same test has been executed again later on when new features has been added.

## Test 

### Test cases

|Tests for Epic [#3](https://github.com/MartinaB91/project4-my-blog/issues/3) Sign in with username||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: Sign in with username Admin| [#55](https://github.com/MartinaB91/project4-my-blog/issues/55)| 
|Test: Sign in with username Blogger|[#56](https://github.com/MartinaB91/project4-my-blog/issues/56)|

|Tests for Epic [#37](https://github.com/MartinaB91/project4-my-blog/issues/37) Ability to CRUD blog posts as Blogger||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: Warning message create post Blogger| [#57](https://github.com/MartinaB91/project4-my-blog/issues/57)| 
|Test: Create post Blogger | [#58](https://github.com/MartinaB91/project4-my-blog/issues/58) |
|Test: Update post Blogger| [#59](https://github.com/MartinaB91/project4-my-blog/issues/59) |
|Test: Delete post Blogger| [#60](https://github.com/MartinaB91/project4-my-blog/issues/60) |
|Test: Searching on a post as a Blogger| [#61](https://github.com/MartinaB91/project4-my-blog/issues/61) |
|Test: Searching on a post content as a Blogger| [#70](https://github.com/MartinaB91/project4-my-blog/issues/70) |
|Test: Searching on posts by author as a Blogger| [#71](https://github.com/MartinaB91/project4-my-blog/issues/71) |
|Test: Searching on a category as a Blogger| [#72](https://github.com/MartinaB91/project4-my-blog/issues/72) |

|Tests for Epic [#6](https://github.com/MartinaB91/project4-my-blog/issues/6) Ability to CRUD blog posts as Admin ||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: Warnings message create post Admin| [#63](https://github.com/MartinaB91/project4-my-blog/issues/63)| |
|Test: Create post Admin| [#62](https://github.com/MartinaB91/project4-my-blog/issues/62)| | 
|Test: Update post as Admin| [#64](https://github.com/MartinaB91/project4-my-blog/issues/64)| | 
|Test: Delete post as Admin| [#65](https://github.com/MartinaB91/project4-my-blog/issues/65)| | 
|Test: Searching on a post title as a Admin| [#66](https://github.com/MartinaB91/project4-my-blog/issues/66)| | 
|Test: Searching on a post content as a Admin| [#67](https://github.com/MartinaB91/project4-my-blog/issues/67)| |
|Test: Searching on posts by author as a Admin| [#68](https://github.com/MartinaB91/project4-my-blog/issues/68)| |
|Test: Searching on a category as a Admin| [#69](https://github.com/MartinaB91/project4-my-blog/issues/69)| |

| Tests for Epic [#7](https://github.com/MartinaB91/project4-my-blog/issues/7) Display blog post properties timestamp & category||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: View posts by category| [#73](https://github.com/MartinaB91/project4-my-blog/issues/73) |
|Test: Select category from list when creating blog post Blogger| [#74](https://github.com/MartinaB91/project4-my-blog/issues/74) |
|Test: View timestamp on posts| [#75](https://github.com/MartinaB91/project4-my-blog/issues/75) |
|Test: Create category Admin| [#76](https://github.com/MartinaB91/project4-my-blog/issues/76) |


| Tests for Epic [#5](https://github.com/MartinaB91/project4-my-blog/issues/5) Implement functionality for comment and like||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: View comment section Blogger| [#77](https://github.com/MartinaB91/project4-my-blog/issues/77) |
|Test: Leave a comment Blogger on Home and Post by category page |[#78](https://github.com/MartinaB91/project4-my-blog/issues/78) |
|Test: Leave a Comment post Blogger on My blog post|[#87](https://github.com/MartinaB91/project4-my-blog/issues/87)|
|Test: Leave a comment Blogger on Blog post page(detail)|[#88](https://github.com/MartinaB91/project4-my-blog/issues/88)|
|Test: Like post Blogger Home and Post by category page| [#79](https://github.com/MartinaB91/project4-my-blog/issues/79) |
|Test: Like post Blogger on My blog post| [#89](https://github.com/MartinaB91/project4-my-blog/issues/89) |
|Test: Like post Blogger Blog post page(detail)| [#90](https://github.com/MartinaB91/project4-my-blog/issues/90) |



|Test for Epic [#46](https://github.com/MartinaB91/project4-my-blog/issues/46) View Bloggers personal posts & post status||
| ----------- | ----------- |
|**Test name** |**Test id:** |
|Test: View my posts Blogger |[#82](https://github.com/MartinaB91/project4-my-blog/issues/82) |
|Test: View published/not published posts Blogger |[#83](https://github.com/MartinaB91/project4-my-blog/issues/83) |

Test results [here](/testing/TEST_RECORDS.md)

### Responsiveness tests

Responsiveness has been tested with help of [Responsivepx](https://www.responsivepx.com/) and [Chrome DevTools](https://developer.chrome.com/docs/devtools/). 

Devtools has been used for testing devices from small phone(<360px) to large tablet (1024px). Responsivepx has been used more exploratory, by increasing and decreasing width and height to various sizes. 

Tests has also been conducted on the following physical devices:
- Samsung s10
- Samsung s20
- Samsung s20 Ultra 
- Asus 17" Laptop
- External screen 22"

### Exploratory tests 

Exploratory tests has been done to try to find behaviour not covered in automatic testing and functional testing. Focus has been on those areas that often are used and were errors can do a lot of harm. I have also tried to use the app "wrong" to see what happens.

Test results [here](/testing/TEST_RECORDS.md)

### Usability testing

In this test three independent users have been presented with some tasks to do in the blog portal. During the testing the person has been observed to see if any usability improvements can be found. The main focus on these tests is to see if the site is easy to navigate and operate. Which is important to get recurrent users. Before the test start, the test user will be informed that this is not a test of how well they perform the tasks but a way to find improvements on the site. 

The user was tasked to perform the following:
1.	Create an account.
2.  Find all posts in category "Dahlias"
3.	Create a blog post
4.  Find the page where you can see all your blog posts
5.	Update the blog post you created
6.  Leave a comment on a blog post
7.  Like a blog post
8.  Sign out from your account

Test results [here](/testing/TEST_RECORDS.md)

### Automatic tests

For running automatic tests pytest was used. 

For code coverage this command was used "pytest --cov-config=.coveragerc. --cov=APPNAME --cov-report=html" and in the coveragerc-file test-files and migration-files were excluded from the reports. 

The code coverage is quite low in some parts. This was expected since automated testing was started to late in the development process. Therefore, it was a bit neglected. 

However extensive functional tests and exploratory tests has been conducted so the test quality is high but more automatic tests would have been helpful during the development. 

#### Blog

<img src="/workspace/project4-my-blog/testing/coverage/coverage_blog.PNG">

#### Blog post

<img src="/workspace/project4-my-blog/testing/coverage/coverage_blog_post.PNG">

#### Home

<img src="/workspace/project4-my-blog/testing/coverage/coverage_home.PNG">

#### Profiles 

<img src="/workspace/project4-my-blog/testing/coverage/coverage_profiles.PNG">

### Lighthouse reports

Since the purpose of the blog app is to showcase nice pictures, the performance is lower due to many pictures loading. During the validation process I managed to improve this significantly, when starting the video header was three times the size and images were already compressed but now are compressed in Webp-format. No more steps will be taken to improve this since this will go against the purpose of the site and the improved results are quite high. 

If there was more time to develop the site a first step would be to prevent users uploading to large images and in bad formats. A more user-friendly approach would be to include a third party tool to convert and compress pictures.  

Since the above mentioned is not fixed or implemented it???s up to the administrator to not approve posts with to larges pictures uploaded. Not doing so will result in bad performance. 

#### Home page 

<img src="/workspace/project4-my-blog/testing/lighthouse_reports/index_LH.PNG">

#### Blog post detail page 

<img src="/workspace/project4-my-blog/testing/lighthouse_reports/blog_post_detail_LH.PNG">

#### Posts by category page

<img src="/workspace/project4-my-blog/testing/lighthouse_reports/post_by_category_LH.PNG">

#### My blog page

<img src="/workspace/project4-my-blog/testing/lighthouse_reports/my_blog_page_LH.PNG">

#### Others 

All form pages (create, update, delete, settings) have been tested using Lighthouse and received a score above 90% for all categories tested. 

### Solved bugs during development
- [#43](https://github.com/MartinaB91/project4-my-blog/issues/43) Like-btn don't "checked"
- [#44](https://github.com/MartinaB91/project4-my-blog/issues/44) Can't update img on post as Blogger
- [#50](https://github.com/MartinaB91/project4-my-blog/issues/50) Page not loading when user not signed 
- [#84](https://github.com/MartinaB91/project4-my-blog/issues/84) Pagination on "My Blog" not working


## Validation

### Html

All pages has been validated using [W3C](https://validator.w3.org/) without errors or warning. See results [here](/testing/validation/VALIDATION.md).

### CSS

CSS has been validated using [W3C](https://validator.w3.org/) without errors or warning. See results [here](/testing/validation/VALIDATION.md).

### JavaScript

All JavaScript code has been validated using [JSHint](https://jshint.com/) without errors or warnings.

### Python
GitPod PROBLEMS reports following errors when 'objects' is used "Class 'Category' has no 'objects' member", this is an error that is safe to ignore according to Google and student channel. 
    
In settings.py there are a few line too long warnings for the URLs. For example "'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',"
Any changes to make this line shorter with linebreaks would make it less readable. Therefore they were ignored. 

All Python code has been validated according to PEP8 using [PEP8 Online](http://pep8online.com/) without any warnings except from line too long mentioned above. 


