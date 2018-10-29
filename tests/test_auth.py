import json
from .base_tests import CLI_Chat_Base

sample_user = [
                {
                "email":"test@mail.com",
                "password":"pass",
                "password2":"pass",
                "role":"admin"
                },
                {
                "email":"",
                "password":"pass",
                "password2":"pass",
                "role":"admin"
                },
                {
                "email":"test@mail.com",
                "password":"",
                "password2":"pass",
                "role":"admin"
                },
                {
                "email":"test@mail.com",
                "password":"pass",
                "password2":"",
                "role":"admin"
                },
                {
                "email":"test@mail.com",
                "password":"pass",
                "password2":"pass",
                "role":""
                },
                {
                "email":"test@mail.com",
                "password":"pass",
                "password2":"pass1",
                "role":"admin"
                },
                {
                "email":"testmail.com",
                "password":"pass",
                "password2":"pass",
                "role":"admin"
                },
                {
                "email":"test@mailcom",
                "password":"pass",
                "password2":"pass",
                "role":"admin"
                }
            ]

sample_users_details = [
                {
                "email":"test1@mail.com",
                "password":"pass",
                "password2":"pass",
                "role":"admin"
                },
                {
                "email":"test2@mail.com",
                "password":"pass",
                "password2":"pass",
                "role":"moderator"
                },
                {
                "email":"test3@mail.com",
                "password":"pass",
                "password2":"pass",
                "role":"user"
                },
                {
                "email":"test1@mail.com",	
                "password":"pass"
                },
                {
                "email":"test2@mail.com",	
                "password":"pass"
                },
                {
                "email":"test3@mail.com",	
                "password":"pass"
                }
            ]
        
sample_login = [
                {
                "email":"test1@mail.com",	
                "password":"pass"
                },
                {
                "email":"",	
                "password":"pass"
                },
                {
                "email":"test1mail.com",	
                "password":""
                },
                {
                "email":"test1mailcom",	
                "password":"pass"
                },
                {
                "email":"teste1@mailcom",	
                "password":"pass"
                },
                {
                "email":"test1@mail.com",	
                "password":"pass1"
                }
            ]

register_url = '/register'
login_url  = '/login'

class Test_Authentication(CLI_Chat_Base):
    def test_registration_successfully(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[0]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 201)
        
    def test_registration_email_empty(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[1]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_registration_password_empty(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[2]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)

    def test_registration_password2_empty(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[3]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_registration_role_empty(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[4]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_registration_passwords_dont_match(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[5]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_registration_wrong_email_format(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[6]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_registration_wrong_email_format2(self):
        response = self.client.post(register_url, data=json.dumps(sample_user[7]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    #  #  #
    def test_login_successfully(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[0]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 201)
        
    def test_login_email_empty(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[1]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_login_password_empty(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[2]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)

    def test_login_wrong_email_format(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[3]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
    
    def test_login_wrong_email_format2(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[4]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 403)
       
    def test_login_wrong_credentials(self):
        response = self.client.post(login_url, data=json.dumps(sample_login[5]), content_type='application/json')
        response_data1 = json.loads(response.data)
        #self.assertEqual("created", response_data1["message"])
        self.assertEqual(response.status_code, 401)
       