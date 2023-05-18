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

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. Categories tested are:
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
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML code used in this project. Code was entered manually in Validate by Direct Input field.
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
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. Code was entered manually in Validate by Direct Input field.

<details><summary>CSS code results</summary><img src="media/tests/validations/css_validation.webp"></details>

---
### PEP8 Python Linter Test
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check if Python code meets PEP8 standards.

#### Blog App
<details><summary> admin.py</summary><img src="media/tests/validations/pep8/blog_admin.webp"></details>
<details><summary> forms.py</summary><img src="media/tests/validations/pep8/blog_forms.webp"></details>
<details><summary> models.py</summary><img src="media/tests/validations/pep8/blog_models.webp"></details>
<details><summary> urls.py</summary><img src="media/tests/validations/pep8/blog_url.webp"></details>
<details><summary> views.py</summary><img src="media/tests/validations/pep8/blog_view.webp"></details>




[Back to top ⇧](#content)