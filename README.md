# youtube_download_manager

<h4>How to run</h4>
<ul>
    <li>go to project path</li>
    <li> python3 src/com/download.py -link "https://youtu.be/KOdfpbnWLVo"</li>
</ul>

<h4>Arguments</h4>
<ul>
    <li><b>-link </b> : youtube link</li>
    <li>
        <b>-audioOnly </b> : only download audio file which is by default <b>False</b>.
        <ul>
            <li>True<br>Only Download Audio</li>
            <li>False<br>Video will be dowload with audio</li>
        </ul>
    </li>
     <li>
        <b>-quality </b> : avialable quality in that video that you want download, default is <b>d</b>.
        <ul>
            <li>d<br>Default Quality</li>
            <li>l<br>low quality</li>
            <li>h<br>heigh quality</li>
        </ul>
    </li>
    <li><b>Heigh Quality Audio : </b> python3 src/com/download.py -link "https://youtu.be/KOdfpbnWLVo" -audioOnly True -quality "h"</li>
    <li><b>Heigh Quality Video : </b> python3 src/com/download.py -link "https://youtu.be/KOdfpbnWLVo" -quality "h"</li>
    <li><b>Low Quality Video : </b> python3 src/com/download.py -link "https://youtu.be/KOdfpbnWLVo" -quality "l"</li>
</ul>

<h4>Dependencies</h4>
<ul>
    <li>pip install pytube3</li>
</ul>

