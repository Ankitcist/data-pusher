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
      <td>GET</td>
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
    <tr>
      <td>Explanation</td>
      <td><p>Fetch all accounts</p></td>
    </tr>
  </tbody>
</table>
<hr>

<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/accounts/"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Create account</p></td>
    </tr>
  </tbody>
</table>
<hr>

<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/accounts/{account_id}"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>PUT</td>
    </tr>
    <tr>
      <td>Query Params</td>
      <td>account_id: int</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Update account</p></td>
    </tr>
  </tbody>
</table>
<hr>

<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/accounts/{account_id}"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>DELETE</td>
    </tr>
    <tr>
      <td>Query Params</td>
      <td>account_id: int</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "email": "string",
            "name": "string"
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Delete account</p></td>
    </tr>
  </tbody>
</table>
<hr>

<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/destinations/"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Query Params</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          [{
            "account_id": 3,
            "url": "https://reqres.in/api/users",
            "http_method": "POST",
            "headers": {
              "Content-Type": "application/json",
              "Authorization": "Bearer your_app_secret_token_here"
            }
          }]
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Fetch all destinations</p></td>
    </tr>
  </tbody>
</table>
<hr>

<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/destinations/"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Create destination</p></td>
    </tr>
  </tbody>
</table>

<hr>
<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/destinations/{destination_id}"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>PUT</td>
    </tr
    <tr>
      <td>Query Params</td>
      <td>destination_id: int</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Update destination</p></td>
    </tr>
  </tbody>
</table>

<hr>
<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/destinations/{destination_id}"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>DELETE</td>
    </tr
    <tr>
      <td>Query Params</td>
      <td>destination_id: int</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          {
            "account_id": 0,
            "url": "string",
            "http_method": "string",
            "headers": {}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>Delete destination</p></td>
    </tr>
  </tbody>
</table>

<hr>
<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/destinations/accounts/{account_id}"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>"GET"</td>
    </tr
    <tr>
      <td>Query Params</td>
      <td>account_id: int</td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          [
            {
              "account_id": 0,
              "url": "string",
              "http_method": "string",
              "headers": {}
            }
          ]
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>For given account_id, fetch all destinations</p></td>
    </tr>
  </tbody>
</table>

<hr>
<table>
  <tbody>
    <tr>
      <td>Endpoint</td>
      <td>"/server/incoming_data/"</td>
    </tr>
    <tr>
      <td>Method</td>
      <td>POST</td>
    </tr
    <tr>
      <td>Query Params</td>
      <td>app_secret_token: str</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>
        <pre>
          {
            "data": {"key" : "value"}
          }
        </pre>
      </td>
    </tr>
    <tr>
      <td>Response</td>
      <td>
        <pre>
          "Success"
        </pre>
      </td>
    </tr>
    <tr>
      <td>Explanation</td>
      <td><p>fetch the account, corresponding to app_secret_token. then fetch all destinations, corresponding to this account, and send the incoming_data to its destinations.</p></td>
    </tr>
  </tbody>
</table>


