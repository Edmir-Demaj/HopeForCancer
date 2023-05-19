# HopeForCancer - Testing

[Return to README.md](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Automated Testing](#automated-testing)
  - [HTML Validator](#html-validator)
  - [CSS Validator](#css-validator)
  - [Python Validator](#python-validator)
 - [Manual Testing (BDD)](#manual-testing-bdd)
    - [Testing User Stories](#testing-user-stories)
    - [Full Testing](#full-testing )
- [Features Testing](#features-testing)

---

## Performance

### Google's Lighthouse Performance
To assess the performance of the website, the [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) tool was utilized. The website received a remarkable performance score of `99 on desktop devices`, indicating excellent performance. However, on mobile devices, the score was `88`, indicating room for improvement. The main contributing factor to this score was identified as the large size of user-uploaded images, which had a significant impact on performance. To address this issue, a future plan is to implement a feature that automatically converts images of any format to the more optimized WebP format.

During the evaluation process, the website underwent testing in various categories, including:
- Performance
- Accessibility
- Best practices
- SEO
- Progressive Web App

#### Desktop Results:
![Lighthouse Desktop Result](media/tests/desktop_lighthouse.webp).

#### Mobile Results:
![Lighthouse Mobile Result](media/tests/mobile_lighthouse.webp).

## Automated Testing

### HTML Validator
The HTML code used in this project was manually entered into the [W3C Markup Validation Service](https://validator.w3.org/) for validation. After the validation process, minor errors and warnings were identified. However, they have been addressed and resolved. Below are the screenshots of each page along with the corresponding validation results:

<details><summary>Home page</summary><img src="media/tests/validations/home_page_html.webp"></details>
<details><summary>About us page</summary><img src="media/tests/validations/about_html_validator.webp"></details>
<details><summary>Cancer Info page</summary><img src="media/tests/validations/info_validation.webp"></details>
<details><summary>Blog page</summary><img src="media/tests/validations/blog_html_validation.webp"></details>
<details><summary>Contact page</summary><img src="media/tests/validations/contact_html_validator.webp"></details>
<details><summary>Post Detail page</summary><img src="media/tests/validations/post_detail_html_validation.webp"></details>
<details><summary>Create Post page</summary><img src="media/tests/validations/create_post_html_validation.webp"></details>
<details><summary>Edit comment page</summary><img src="media/tests/validations/edit_comment_html_validation.webp"></details>

---

### CSS Validator
The CSS code utilized in this project was manually inputted into the [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) for validation. Following the validation process there were no errors detected in code. Presented below is the screenshot of the results: 

<details><summary>CSS validation results</summary><img src="media/tests/validations/css_validation.webp"></details>

---
### Python Validator
The Python code utilized in this project was manually inputted into the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) for validation. This validation checks if code written in Python met PEP8 requirements. Validation was divided in 3 stages, one for each app and each Python file inside. Following the validation process there were no errors detected in code. Presented below are the screenshots of each app/file with the results:

#### Blog App
<details><summary> admin.py</summary><img src="media/tests/validations/pep8/blog_admin.webp"></details>
<details><summary> forms.py</summary><img src="media/tests/validations/pep8/blog_forms.webp"></details>
<details><summary> models.py</summary><img src="media/tests/validations/pep8/blog_models.webp"></details>
<details><summary> urls.py</summary><img src="media/tests/validations/pep8/blog_url.webp"></details>
<details><summary> views.py</summary><img src="media/tests/validations/pep8/blog_view.webp"></details>

---

#### Contact App
<details><summary> admin.py</summary><img src="media/tests/validations/pep8/contact_admin.webp"></details>
<details><summary> forms.py</summary><img src="media/tests/validations/pep8/contact_forms.webp"></details>
<details><summary> models.py</summary><img src="media/tests/validations/pep8/contact_models.webp"></details>
<details><summary> urls.py</summary><img src="media/tests/validations/pep8/contact_urls.webp"></details>
<details><summary> views.py</summary><img src="media/tests/validations/pep8/contact_view.webp"></details>

---

#### Other_Pages App
<details><summary> admin.py</summary><img src="media/tests/validations/pep8/other_pages_admin.webp"></details>
<details><summary> models.py</summary><img src="media/tests/validations/pep8/other_pages_models.webp"></details>
<details><summary> urls.py</summary><img src="media/tests/validations/pep8/other_pages_urls.webp"></details>
<details><summary> views.py</summary><img src="media/tests/validations/pep8/other_pages_view.webp"></details>

[Back to top ⇧](#content)

## Manual Testing (BDD)


Behaviour Driven Development (BDD) is a testing approach that enables the evaluation of user stories in a user-friendly manner, making it accessible to individuals without technical expertise. This methodology facilitates the testing of various app features by breaking down complex scenarios into understandable and relatable behaviors.

### Testing User Stories

| User Story | BDD Test | Pass |
| :--- | :--- | :--- |
| `First Time User` |
|  |  |  |
| As a First-Time  User, I want to be able to easily understand the purpose of the website, so that I can get a fast understanding of what is about. | Given that I'm a first time User and when I open Home page i can see clear messages and meaningful images  with a nice logo so I understand what is about the site. | Pass |
| As a First-Time User, I want to be able to get a brief introduction about cancer, so that I can understand what this website cover and if I want to stay or leave the site. | Given that I'm a first time User and when I scroll down Home page i can see 3 different cards with brief introduction to the most important content about the site purpose which increase my curiosity to read more. | Pass |
| As a First-Time User, I want to easily understand the mission of the website, so that I can understand if is the right website I am looking for. | Given that I'm a first time User and to understand more about website mission i can easily get this information from About us page with very clear and short message. | Pass |
| As a First-Time User, I want to understand the values of this website, so that I can understand how the site treats cancer in the community and if is helpful for me. | Given that I'm a first time User and when I scroll down the About us page i can easily identify the Values of the website. | Pass |
| As a First-Time User, I want to be able to easily navigate the site without to much confusions. | Given that I'm a first time User and when I enter in this site I can see an easy to navigate navbar with links and many helpful buttons/links around the site to access additional resources or to return back to the previous page. | Pass |
| As a First-Time User, I want to be able to Register for an account. | Given that I'm a first time User and on navbar I can easily identify the 'Sign up' link with a simple form to register my account. | Pass |
|`Returning User`|
|  |  |  |
| As a returning User, I want to be able to Login to my account so i can get easily access to website restricted features. | Given that I'm a site User and every time I use the site can easily Login with simple form.| Pass |
| As a returning User, I want to see latest post from other users without need to scroll the Blog page. | Given that I'm a site User and every time I use the site I can view the latest 3 posts updated in Home page. | Pass |
| As a returning User, I want to stay updated with latest news and accurate information about cancer. | Given that I'm a site User and every time I use the site can select the topic I'm interested from a dropdown menu and can easily visit other professional websites so I can get the information I want. | Pass |
| As a returning User, I want to create a post and engage with community. | Given that I'm a site User and every time I return back can click on create post buttons around the site and share my stories with others. | Pass |
| As a returning User, I want to be able to access the site from different devices. | Given that I'm a site User and I am able to access the site in different devices without losing layout design or funcionality. | Pass |
| As a returning User, I want to comment on a post so I can share my thoughts about the post. | Given that I'm a site User and when I loggin to my account I can just click the post I want to leave a comment and submit it via an easy form. | Pass |
| As a returning User, I want to understand when my interactions with site are finished or failed. | Given that I'm a site User and when I login or logout, when I like posts, leave comments and more I'm always provided with short clear feedback message. | Pass |
| As a returning User, I want to be able to edit one of my posts or comments. | Given that I'm a site User and when I want to edit a comment or post I can easily do it via edit buttons. | Pass |
| As a returning User, I want to be able to view which post has more likes or comments so might be interesting to read it. | Given that I'm a site User and when I navigate through posts I can see the number of likes and comments for each post. | Pass |
|`Site Admin` |
| As a site Admin, I want to be able to have my dashboard so I can easily access site funcionality. | Given that I'm a site Admin and when I login to my admin site with my unique credentials I'm able to see my dashboard and navigate to different parts of funcionality the site provides. | Pass |
| As a site Admin, I want to be able to view all Users of the site who have already an account registered. | Given that I'm a site Admin and on my dashboard I can view all site Users who have an account registered and their details. | Pass |
| As a site Admin, I want to be able to create, read, update posts. | Given that I'm a site Admin and on my dashboard I can apply all CRUD funcionality. | Pass |
| As a site Admin, I want to be able to review posts before posting them to maintain the quality of content on the website. | Given that I'm a site Admin and on my dashboard I can view all posts with  status 'Draft', can review them and post after. | Pass |
| As a site Admin, I want to be able to review comments before posting them to maintain the quality of content on the website. | Given that I'm a site Admin and on my dashboard I can view all comments with  status 'Draft', can review them and make public. | Pass |
| As a site Admin, I want to be able to update website values or FAQs. | Given that I'm a site Admin and on my dashboard I access this two sections and update or add new ones when is required to keep site content up-to-date. | Pass |
| As a site Admin, I want to be able to receive messages sent by Users so i can respond to them via email. | Given that I'm a site Admin and on my dashboard I can view all messages sent via contact form on Contact page and their details. | Pass |
|  |  |  |

- - -

### Full Testing

Full testing was performed in different browsers and devices to make sure everything works as wanted.

* Laptop:
  * Lenovo Ideapad 5i 16 inch screen
* Mobile Devices:
  * Samsung A71.
  * iPhone 12 pro.
  * Samsung Galaxy s20.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox
* Microsoft Edge
* Opera Browser

## Features Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| HopeForCancer Logo | When clicked the user will be redirected to the home page. | Clicked Logo  | Redirected to the Home page. | Pass |
| Home page link | When clicked the user will be redirected to the home page.| Clicked Home page link | Redirected to the Home page. | Pass |
| About us page link | When clicked the user will be redirected to the About us page. | Clicked About us page link | Redirected to the About us page. | Pass |
| Cancer information page link | When clicked the user will be redirected to the Cancer information page. | Clicked Cancer information page link | Redirected to Cancer information page. | Pass |
| Blog page link | When clicked the user will be redirected to the Blog page. | Clicked Blog page link | Redirected to the Blog page. | Pass |
| Contact page link | When clicked the user will be redirected to the Contact page. | Clicked Contact page link | Redirected to the Contact page. | Pass |
| Login page link (Only shown if user is not loggedin) | When clicked the user will be redirected to the Login page. | Clicked Login page link | Redirected to the Login page. | Pass |
| Signup page Link (Only shown if user not loggedin) | When clicked the user will be redirected to the Signup page. | Clicked Signup page link | Redirected to the Signup page. | Pass |
| Logout page Link (Logged in users only) | When clicked the user will be redirected to Logout page to confirm they want to logout. If they confirm will redirect to Home page and a flash message displayed to let the user know they have been logged out successfully. If they don't confirm will be redirected to Home page. | Clicked Logout page link | Redirected to the Home page and a flash message displayed to let me know I have been logged out. Redirected to the Home page if I cancell logout execution. | Pass |
| Username link (Logged in users only) | When clicked the user will be redirected to Blog page. This will be a feature to implement so user will have their own page to see their posts or comments. | Clicked Username link | Redirected to the Blog page | Pass |
| `Footer` |
|  |  |  |  |  |
| Useful links | When Useful links clicked the user will be redirected to the related page clicked. | Clicked all Useful links one by one | Redirected to the related page as thier name shows. | Pass |
| Follow us links | When Follow us links clicked the user will be redirected to the social media clicked and open in a new tab. | Clicked all Follow us links one by one | Redirected to the related socail media as thier name shows and they open in a new tab. | Pass |
| Privacy & Policy page link | When Privacy & Policy page link clicked the user will be redirected to Privacy & Policy page and open a new modal window. | Clicked Privacy & Policy page link | Redirected to the Privacy & Policy page where a new modal window modal open. | Pass |
| Copyright year | The copyright should display the correct year - this is a javascript function that checks what the current year is and injects it into the footer | Checked the year | Displaying the correct year | Pass |
| `Home Page` |
|   |   |   |   |
| Get more info link  | When clicked the user will be redirected to the Cancer Information page. | Clicked Get more info link  | Redirected to the Cancer Information page. | Pass |
| More about cancer link  | When clicked the user will be redirected to the Cancer Information page, what is cancer. | Clicked More about cancer link  | Redirected to the Cancer Information page, what is cancer. | Pass |
| More about cancer types link  | When clicked the user will be redirected to the Cancer Information page, cancer types section. | Clicked More about cancer types link  | Redirected to the Cancer Information page, cancer types section. | Pass |
| More about early detection link  | When clicked the user will be redirected to the Cancer Information page, early detection section. | Clicked More about early detection link | Redirected to the Cancer Information page, early detection section. | Pass |
| Understanding cancer dropdown links  | When clicked the user will be redirected to the National Cancer Institute website, to the specific sections. New site opens in a new tab. | Clicked  Understanding cancer dropdown links one by one | Redirected to the National Cancer Institute website, to the specific sections. Opens in a new tab. | Pass |
| Create post link | When clicked the user will be redirected to the Create post page if they are loggedin, if not they will redirect to login page. | Clicked  Create post link | Redirected to the Login page if I'm not loggedin, redirect to Create post page if I'm loggedin. | Pass |
| Discover stories link | When clicked the user will be redirected to the Blog page. | Clicked  Discover stories link | Redirected to the Blog page. | Pass |
| Go to Top button | When clicked the user will be moved to top of the page. | Clicked  Go to Top button | Redirected to the top of the page. | Pass |
| Lates posts link | When clicked the user will be redirected to the Post detail page. | Clicked  on card or title | Redirected to the Post details page. | Pass |
| `About us Page` |
| Follow Edmir other platforms links | When clicked the user will be redirected to the other platforms and open in new tab. | Clicked on Follow Edmir other platforms links one by one | Redirected to the each social media and open in a new tab. | Pass |
| `Cancer Information Page` |
| Explore more links |  When clicked the user will be redirected to the National Cancer Institute website, to the specific sections. New site opens in a new tab. | Clicked on Explore more links one by one | Redirected to the National Cancer Institute website, to the specific sections. Opens in a new tab. | Pass |
| `Login Page` |
| Username input - empty | This is a required field so the form should not submit if empty. | Tried to submit the form with this field empty | Field error messages tells me 'This field is required'. | Pass |
| Password input empty | This is a required field so the form should not submit if empty. | Tried to submit the form with this field empty | Field error messages tells me 'This field is required'. |  Pass |
| Login button | Saves the user to session and redirects to the Blog page. Flash message shown succesfully signed in. | Submitted form | Redirected to the Blog page and flash message succesfully signed in. | Pass |
| Incorrect username or password used | A flash message should display saying username/or password incorrect - this is defensive programming - not letting user know which input is incorrect. | Incorrect username/password entered | Message flashes to let the user know they have entered an incorrect username/or password. | Pass |
| Link to Sign up page |  This should redirect the user to the Sign up page. | Clicked Sign up link | Redirected to the Sign up page. | Pass |
| `Logout Page` |
| Two links to confirm or no Logout | When 'Yes, I confirm' clicked the user will be redirected to the Home page and succesfully logged out message flashed. When "No, I don't" clicked the user will be redirected to the Home page. | Tried to click both links | Redirected to the Home page respectively. | Pass |
| `Sign up Page` |
| Username input - empty | The username is a required field, so should not submit with no value. | Tried to submit form with no value entered | Field error messages lets user know 'this value is required'. | Pass |
| Username input - used already | If username is in use, message should flash to user. | Entered an in use username | Message flashed to say username already in use. | Pass|
| Email input | The email input should include an email address. | Entered plain text | Field error messages tells user to use an email @ address here. | Pass |
| Password input - length | This field should be at least 8 characters long | Entered password less than 8 characters long | Field error messages tells user the password should be at least 8 characters long. | Pass |
| Password input - empty | The password is a required field, so should not submit with no value. | Tried to submit form with no value entered | Field error messages lets user know 'This value is required'. | Pass |
| Password (again) | The password (again) is a required field and should match with Password field | Tried to submit form with different password values entered | Field error messages lets user know 'Password doesn't match'. | Pass |
| Password - too common | The password should be a mixture of numbers, letters, characters. | Tried to submit form with only numeric password values (1,2,3,4,5,6,7,8) | Field error messages lets user know 'This password is too common'. | Pass |
| Sign up button | Should redirect user to the Blog page and a registration successful message flashed | Created new user and submitted form | Redirected to the Blog in page and message flashed | Pass |
| `Contact Page` |
| Search feature | A search is performed when the user enters a search term | Searched for rabbits | The search returns book results | Pass |
| `Error Page` |
| Home page link | Redirects the user to the home page | Clicked link | Redirected to home page | Pass |