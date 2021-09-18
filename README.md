# imdb-rest-api

<h3>This is IMDB clone for rest-api built in Django Rest Framework </h3>
<b>1. Accounts</b>

For accounts section we prefer the use of Postman application \
Download link: https://www.postman.com/downloads/
<ul>
    <li>Registration: http://127.0.0.1:8000/api/account/register/</li>
    <li>Login: http://127.0.0.1:8000/api/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/api/account/logout/</li>
</ul>
<br>

<b>2. Stream Platforms</b>
<ul>
    <li>Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/&lt;int:streamplatform_id&gt;/</li>

</ul>
<br>

<b>3. Watch List</b>
<ul>
    <li>Create & Access List: http://127.0.0.1:8000/api/watch/list/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/&lt;int:movie_id&gt;/</li>
    <li>Search through url: http://127.0.0.1:8000/api/watch/list2/?search=title
</ul>
<br>

<b>4. Reviews</b>
<ul>
    <li>Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/&lt;int:movie_id&gt;/review-create/</li>
    <li>List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/&lt;int:movie_id&gt;/reviews/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/&lt;int:review_id&gt;/</li>
</ul>
<br>

<b>5. User Review</b>
<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example</li>
</ul>
<br>

Screenshots:

![stream](https://user-images.githubusercontent.com/65828169/132946326-33642353-5972-49ad-8960-e7566bf2063a.JPG)
![list](https://user-images.githubusercontent.com/65828169/132946353-08650cee-dc71-467c-b926-b42faeefaa71.JPG)
![search2](https://user-images.githubusercontent.com/65828169/132946415-9b898aae-197c-489c-8bf8-b8564fab2898.JPG)


