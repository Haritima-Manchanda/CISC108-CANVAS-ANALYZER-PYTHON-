


<p>To simplify accessing the Canvas API, we have provided the <code>canvas_requests</code> module that wraps the <code>requests</code> module. In particular, 3 functions are exposed that let you conveniently access the Canvas website programatically.</p>

<p>When you are finished the project, you will be able to use your code to analyze your own Canvas data. If you want to try this, you will need to obtain a <i>Canvas API Token</i>. These tokens are free and easy to obtain by following <a href="https://community.canvaslms.com/docs/DOC-10806-4214724194" target="_blank" rel="noopener noreferrer">these instructions</a>. Once you have your token (a string of roughly 70 random characters), you can pass it in to your <code>main</code> function instead of <code>'harry'</code>, <code>'hermione'</code>, or <code>'ron'</code>.</p>

<img src="server_diagram.png" />


<h3>get_user</h3>
<p><strong>Description:</strong> The function <code>get_user</code> retrieves a User dictionary.</p>
<p><strong>Syntax:</strong>
<pre>canvas_requests.get_user(user_id)</pre>
<p><strong>Parameters:</strong><br>
- user_id (<code>str</code>): The user_id or token to retrieve a User dictionary for.</p>
<p><strong>Returns:</strong> <code>dict</code></p>
<p><strong>Example:</strong>
<pre style="color: #000000; background: #ffffff;">
>>> canvas_requests.get_user(<span style="color: #2a00ff;">"hermione"</span>)
{
  <span style="color: #3f7f59;"># The unique ID of the user</span>
  <span style="color: #2a00ff;">"id"</span>: 42,
  <span style="color: #3f7f59;"># The full name of the user</span>
  <span style="color: #2a00ff;">"name"</span>: <span style="color: #2a00ff;">"Hermione Granger"</span>,
  <span style="color: #3f7f59;"># The shortened name of the user</span>
  <span style="color: #2a00ff;">"short_name"</span>: <span style="color: #2a00ff;">"Hermione Granger"</span>,
  <span style="color: #3f7f59;"># Last name, first name</span>
  <span style="color: #2a00ff;">"sortable_name"</span>: <span style="color: #2a00ff;">"granger, hermione"</span>,
  <span style="color: #3f7f59;"># Title, if available</span>
  <span style="color: #2a00ff;">"title"</span>: <span style="color: #2a00ff;">"Student"</span>,
  <span style="color: #3f7f59;"># User-supplied self-description</span>
  <span style="color: #2a00ff;">"bio"</span>: <span style="color: #2a00ff;">"Interested in Magic, Learning, and House Elf Rights"</span>,
  <span style="color: #3f7f59;"># User-supplied primary email</span>
  <span style="color: #2a00ff;">"primary_email"</span>: <span style="color: #2a00ff;">"hgranger@hogwarts.edu"</span>,
  <span style="color: #3f7f59;"># University-managed account id</span>
  <span style="color: #2a00ff;">"login_id"</span>: <span style="color: #2a00ff;">"hgranger@hogwarts.edu"</span>,
  <span style="color: #3f7f59;"># An image URL of the user</span>
  <span style="color: #2a00ff;">"avatar_url"</span>: <span style="color: #2a00ff;">"https://i.imgur.com/gaNCiuW.png"</span>,
  <span style="color: #3f7f59;"># The users default timezone</span>
  <span style="color: #2a00ff;">"time_zone"</span>: <span style="color: #2a00ff;">"Europe/London"</span>
}
</pre>
</p>

<h3>get_courses</h3>
<p><strong>Description:</strong> The function <code>get_courses</code> retrieves a list of Course dictionaries associated with a user (aka the courses they are enrolled in).</p>
<p><strong>Syntax:</strong>
<pre>canvas_requests.get_courses(user_id)</pre>
<p><strong>Parameters:</strong><br>
- user_id (<code>str</code>): The user_id or token to retrieve courses for.</p>
<p><strong>Returns:</strong> <code>list</code></p>
<p><strong>Example:</strong>
<pre style="color: #000000; background: #ffffff;">
>>> canvas_requests.get_courses(<span style="color: #2a00ff;">"hermione"</span>)
[
    {
      <span style="color: #3f7f59;"># The unique ID of the course</span>
      <span style="color: #2a00ff;">"id"</span>: 15,
      <span style="color: #3f7f59;"># The full name of the course</span>
      <span style="color: #2a00ff;">"name"</span>: <span style="color: #2a00ff;">"Potions"</span>,
      <span style="color: #3f7f59;"># The current state of the course, one of:</span>
      <span style="color: #3f7f59;"># 'available', 'unpublished', 'completed', </span>
      <span style="color: #3f7f59;"># or 'deleted'</span>
      <span style="color: #2a00ff;">"workflow_state"</span>: <span style="color: #2a00ff;">"available"</span>
    }, ...
    <span style="color: #3f7f59;"># Rest redacted</span>
]
</pre>
</p>

<h3>get_submissions</h3>
<p><strong>Description:</strong> The function <code>get_submissions</code> retrieves a list of Submission dictionaries associated with a user and the course.</p>
<p><strong>Syntax:</strong>
<pre>canvas_requests.get_submissions(user_id, course_id)</pre>
<p><strong>Parameters:</strong><br>
- user_id (<code>str</code>): The user's name or Canvas token to retrieve courses for.<br>
- course_id (<code>int</code>): The unique integer ID of the course.</p>
<p><strong>Returns:</strong> <code>list</code></p>
<p><strong>Example:</strong>
<pre style="color: #000000; background: #ffffff;">
>>> canavs_requests.get_submissions(<span style="color: #2a00ff;">"hermione"</span>, 15)
[
    {
      <span style="color: #3f7f59;"># The assignment ID that this submission belongs to</span>
      <span style="color: #2a00ff;">"assignment_id"</span>: 270633,
      <span style="color: #3f7f59;"># The user ID that this submission belongs to</span>
      <span style="color: #2a00ff;">"user_id"</span>: 42,
      <span style="color: #3f7f59;"># The number of times the assignment was submitted</span>
      <span style="color: #2a00ff;">"attempt"</span>: 1,
      <span style="color: #3f7f59;"># The raw score assigned to the submission</span>
      <span style="color: #2a00ff;">"score"</span>: 18,
      <span style="color: #3f7f59;"># When this was submitted. None if unsubmitted.</span>
      <span style="color: #2a00ff;">"submitted_at"</span>: <span style="color: #2a00ff;">"2017-09-18T21:22:53Z"</span>,
      <span style="color: #3f7f59;"># When this was graded. None if ungraded.</span>
      <span style="color: #2a00ff;">"graded_at"</span>: <span style="color: #2a00ff;">"2017-09-30T11:43:39Z"</span>,
      <span style="color: #3f7f59;"># The user ID of the grader. None if ungraded.</span>
      <span style="color: #2a00ff;">"grader_id"</span>: 476,
      <span style="color: #3f7f59;"># Whether the assignment was excused</span>
      <span style="color: #2a00ff;">"excused"</span>: False,
      <span style="color: #3f7f59;"># Whether the assignment was late</span>
      <span style="color: #2a00ff;">"late"</span>: False,
      <span style="color: #3f7f59;"># Whether the assignment was missing</span>
      <span style="color: #2a00ff;">"missing"</span>: False,
      <span style="color: #3f7f59;"># The current status of the submissions. Possible</span>
      <span style="color: #3f7f59;"># values of "submitted", "unsubmitted", "graded"</span>
      <span style="color: #2a00ff;">"workflow_state"</span>: <span style="color: #2a00ff;">"graded"</span>,
      <span style="color: #3f7f59;"># A dictionary containing information about the assignment</span>
      <span style="color: #2a00ff;">"assignment"</span>: {
          <span style="color: #3f7f59;"># The unique ID of the assignment</span>
          <span style="color: #2a00ff;">"id"</span>: 270633,
          <span style="color: #3f7f59;"># The full name of the assignment</span>
          <span style="color: #2a00ff;">"name"</span>: <span style="color: #2a00ff;">"#7.5) Programming: Variables and Tracing"</span>,
          <span style="color: #3f7f59;"># The assignment group ID that this assignment belongs to</span>
          <span style="color: #2a00ff;">"assignment_group_id"</span>: 82389,
          <span style="color: #3f7f59;"># The due date of this assignment (can be None)</span>
          <span style="color: #2a00ff;">"due_at"</span>: <span style="color: #2a00ff;">"2017-10-10T00:00:00Z"</span>,
          <span style="color: #3f7f59;"># The lock date of this assignment (can be None)</span>
          <span style="color: #2a00ff;">"lock_at"</span>: <span style="color: #2a00ff;">"2017-09-01T16:40:00Z"</span>,
          <span style="color: #3f7f59;"># The unlock date of this assignment (can be None)</span>
          <span style="color: #2a00ff;">"unlock_at"</span>: None
          <span style="color: #3f7f59;"># The number of possible points for this assignment (can be None)</span>
          <span id="assignment-points_possible" style="color: #2a00ff;">"points_possible"</span>: 5.0,
          <span style="color: #3f7f59;"># A dictionary containing information about the group</span>
          <span style="color: #2a00ff;">"group"</span>: {
              <span style="color: #3f7f59;"># The unique ID of the group</span>
              <span style="color: #2a00ff;">"id"</span>: 82389,
              <span style="color: #3f7f59;"># The full name of the group</span>
              <span style="color: #2a00ff;">"name"</span>: <span style="color: #2a00ff;">"Programming Problems"</span>,
              <span style="color: #3f7f59;"># The assigned weight of this group, relative</span>
              <span style="color: #3f7f59;"># to other groups. Sums to 100, representing</span>
              <span style="color: #3f7f59;"># percents.</span>
              <span style="color: #2a00ff;">"group_weight"</span>: 25,
             }
      }
    }, ...
    <span style="color: #3f7f59;"># Rest redacted</span>
]
</pre>
</p>

<p>The information shown here is an abridged version of the <a href="https://canvas.instructure.com/doc/api/courses.html" target="_blank" rel="noopener noreferrer">official Canvas documentation</a>. You may find it interesting to review the full API. </p>