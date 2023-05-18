# HopeForCancer - Testing

[Return to README.md](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)
  - [Automated Testing](#automated-testing)
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

## Code Validation

### HTML Validation
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

### CSS Validation
The CSS code utilized in this project was manually inputted into the [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) for validation. Following the validation process there were no errors detected in code. Presented below is the screenshot of the results: 

<details><summary>CSS validation results</summary><img src="media/tests/validations/css_validation.webp"></details>

---
### PEP8 Python Linter Test
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