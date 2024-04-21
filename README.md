<h2>Steps to setup code:</h2>
<ul>
  <li> Clone repo</li>
  <li> Go to the cloned folder</li>
  <li> Create venv inside this folder</li>
  <li> Activate venv</li>
  <li> Install all packages using "pip install -r requirements.txt"</li>
  <li> Command to start API server: "python3 main.py startserver"</li>
</ul>


<h2>APIs descriptions</h2>
<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/accounts/"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>"GET"</td>
    </tr>
    <tr>
      <td>Query Params</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          [
            {
              "email": "string",
              "name": "string",
              "id": 0,
              "app_secret_token": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
          ]
        </pre>
      </td>
    </tr>
  </tbody> 
</table>

<hr>
