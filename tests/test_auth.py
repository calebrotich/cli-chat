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
                "email":"",	
                "password":"pass"
                },
                {
                "email":"test1@mail.com",	
                "password":""
                },
                {
                "email":"test1mail.com",	
                "password":"pass"
                },
                {
                "email":"test1@mailcom",	
                "password":"pass"
                },
                {
                "email":"teste1@mail.com",	
                "password":"pass"
                },
                {
                "email":"test1@mail.com",	
                "password":"pass1"
                },
                {
                "email":"test1@mail.com",	
                "password":"pass"
                }
            ]


class Test_Authentication(CLI_Chat_Base):
    def test_registration(self):
        # Test successful register
        response = self.client.post(register_url, data=json.dumps(sample_user[0]), content_type='application/json')
        response_data1 = json.loads(response.data)
        self.assertEqual(
            "Welcome nicoleb!", response_data1["message"])
        self.assertEqual(response.status_code, 201)
        # Test registration with nonexistent role

        response8 = self.client.post(
            self.signupurl, headers=dict(Authorization="Bearer " + token),
            data=json.dumps(dict(
                name='charity marani',
                email='nicoleb@gmail.com',
                role='sWEEper',
                username='nicoleb',
                password='1234',
                confirm_password='1234'
            )),
            content_type='application/json'
        )
        response_data8 = json.loads(response8.data)
        print(response_data8)
        self.assertEqual(response8.status_code, 400)
        self.assertEqual(
            "The role sweeper does not exist.Only admin and attendant roles are allowed", response_data8["message"])
        # Test registration with invalid email
        response2 = self.client.post(
            self.signupurl, headers=dict(Authorization="Bearer " + token),
            data=json.dumps(dict(
                name='charity marani',
                email='chachagmail.com',
                role='attendant',
                username='chacha',
                password='1234',
                confirm_password='1234'
            )),
            content_type='application/json'
        )
        response_data2 = json.loads(response2.data)
        self.assertEqual("Enter a valid email address",
                         response_data2["message"])
        self.assertEqual(response2.status_code, 403)

        # test short password
        result = self.client.post(self.signupurl, headers=dict(Authorization="Bearer " + token),
                                  content_type="application/json",
                                  data=json.dumps({"name": "marani", "username": "maro",
                                                   "email": "maro@gmail.com", "password": "123",
                                                   "confirm_password": "123", "role": "attendant"}))
        my_data = json.loads(result.data)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(
            "The password is too short,minimum length is 4", my_data["message"])

        # test unmatching passwords
        result2 = self.client.post(self.signupurl, headers=dict(Authorization="Bearer " + token),
                                   content_type="application/json",
                                   data=json.dumps({"name": "Mose", "username": "gebby",
                                                    "email": "gebby@to.cm", "password": "Test123",
                                                    "confirm_password": "Test13", "role": "attendant"}))
        my_data2 = json.loads(result2.data)
        self.assertEqual(result2.status_code, 400)
        self.assertEqual(
            "The passwords you entered don't match", my_data2["message"])
        # test for missing fields
        result3 = self.client.post(self.signupurl, headers=dict(Authorization="Bearer " + token),
                                   content_type="application/json",
                                   data=json.dumps({"name": "", "username": "",
                                                    "email": "gebby@to.cm", "password": "Test123",
                                                    "confirm_password": "Test123", "role": "attendant"}))
        my_data3 = json.loads(result3.data)
        self.assertEqual(result3.status_code, 206)
        self.assertEqual(
            "Make sure all fields have been filled out", my_data3["message"])
        # Test for empty data
        result4 = self.client.post(self.signupurl, headers=dict(Authorization="Bearer " + token),
                                   content_type="application/json",
                                   data=json.dumps({}))
        my_data4 = json.loads(result4.data)
        self.assertEqual(result4.status_code, 400)
        self.assertEqual("Fields cannot be empty", my_data4["message"])
        # Test registration using existing username
        response1 = self.client.post(
            self.signupurl, headers=dict(Authorization="Bearer " + token),
            data=json.dumps(dict(
                name='charity marani',
                email='hez@gmail.com',
                role='attendant',
                username='nicoleb',
                password='1234',
                confirm_password='1234'
            )),
            content_type='application/json'
        )
        response_data1 = json.loads(response1.data)
        self.assertEqual(
            "Username already exists. Try a different one.", response_data1["message"])
        # Test registration using existing email
        response2 = self.client.post(
            self.signupurl, headers=dict(Authorization="Bearer " + token),
            data=json.dumps(dict(
                name='charity marani',
                email='nicoleb@gmail.com',
                role='attendant',
                username='jerry',
                password='1234',
                confirm_password='1234'
            )),
            content_type='application/json'
        )
        response_data2 = json.loads(response2.data)
        self.assertEqual(
            "Email already in use. Try a different one.", response_data2["message"])

    def test_user_login(self):
        with self.client:
            # Test success
            response = self.client.post(
                self.loginurl,
                data=json.dumps(self.login_data4),
                content_type='application/json'
            )
            response_data1 = json.loads(response.data)
            token1 = response_data1["token"]

            self.assertEqual(
                "Login successful!Welcome back, nicoleb!", response_data1["message"])
            self.assertEqual(response.status_code, 200)
            # Test attendant can't register user
            responsea = self.client.post(
                self.signupurl, headers=dict(Authorization="Bearer " + token1),
                data=json.dumps(self.register_data),
                content_type='application/json'
            )
            response_dataa = json.loads(responsea.data)
            self.assertEqual(
                "Only an admin can add new users!", response_dataa["message"])
            self.assertEqual(responsea.status_code, 401)

            # Test for empty data
            response2 = self.client.post(
                self.loginurl,
                data=json.dumps(dict()
                                ),
                content_type='application/json'
            )
            response_data2 = json.loads(response2.data)
            self.assertEqual("Fields cannot be empty",
                             response_data2["message"])
            self.assertEqual(response2.status_code, 400)
            # Test for missing fields
            response3 = self.client.post(
                self.loginurl,
                data=json.dumps(dict(
                    username='',
                    password='1234'

                )),
                content_type='application/json'
            )
            response_data3 = json.loads(response3.data)
            self.assertEqual("Username or password missing",
                             response_data3["message"])
            self.assertEqual(response3.status_code, 206)
            # Test for invalid login
            response4 = self.client.post(
                self.loginurl,
                data=json.dumps(dict(
                    username='nicoleb',
                    password='vbnc'

                )),
                content_type='application/json'
            )
            response_data4 = json.loads(response4.data)
            self.assertEqual(
                "The password you entered is incorrect", response_data4["message"])

            # Test for incorrect username
            response5 = self.client.post(
                self.loginurl,
                data=json.dumps(dict(
                    username='ruth',
                    password='1234'

                )),
                content_type='application/json'
            )
            response_data5 = json.loads(response5.data)
            self.assertEqual(
                "Username does not exist in our records", response_data5["message"])

    def test_user_logout(self):
        with self.client:
           # Test logout
            response = self.client.post(
                self.loginurl,
                data=json.dumps(self.login_data4),
                content_type='application/json'
            )
            response_data1 = json.loads(response.data)
            token1 = response_data1["token"]
            response2 = self.client.post(
                self.logouturl, headers=dict(Authorization="Bearer " + token1))
            response_data2 = json.loads(response2.data)
            self.assertEqual("Successfully logged out",
                             response_data2["message"])
            self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        with self.client:
            # Test success
            result = self.client.get(self.allusersurl)
            self.assertEqual(result.status_code, 200)

    def test_get_user_by_username(self):
        with self.client:
            # Test success
            result = self.client.get(self.allusersurl+'/nicoleb')
            self.assertEqual(result.status_code, 200)
            # Test user by noexistent username
            result2 = self.client.get(self.allusersurl+'/amos')
            resp = json.loads(result2.data)
            self.assertEqual(
                "username does not exist in our records", resp["message"])