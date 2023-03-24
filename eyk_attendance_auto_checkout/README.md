<h3>eyk Attendance Auto Checkout</h3>

checks every 5 Minutes if the Limit is reached and if the employee gets checked out

<h5>Release 0.1</h5>
<ul>
<li>Autocheckout based on a hour limit set in the code for Odoo 15</li>
</ul>

<h5>config</h5>

edit the file models/hr_attendance.py <br>
Change the number 9 the line according to your needs<br>
            if delta.total_seconds() >= 9 * 3600: # 9 hours in seconds
            
<br>            
<h5>Additional ideas for future versions</h5> 
<ul>
<li>set hour limit in the ui</li>
<li>ssend an Email to the employee and admin when checkout out</li>
