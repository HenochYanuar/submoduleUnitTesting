import requests

def getApi():
  url = "https://api.restful-api.dev/objects/"
  
  res = requests.get(url)
  
  if res.status_code == 404:
    data = 'Not Found'
  
  data = res.json()
  return data

if __name__ == '__main__':
  print(getApi())










  
# def len_string():
#   str = "Hello World"
#   return len(str)



# def len_joke():
#   joke = get_joke()
#   return len(joke)

# def get_joke():
#   url = 'url/to/api/joke'

#   response = requests.get(url)

#   if response.status_code == 200:
#     joke = response.json()['value'] ['joke']
#   else:
#     joke = 'No Jokes'

#   return joke

# if __name__ == '__main__':
#   print(get_joke())





# import unittest
# from unittest.mock import patch

# from main import len_joke


# class Testjoke(unittest.TestCase):

#   @patch('main.get_joke'):
#   def test_len_joke(self, mock_get_joke):
#     mock_get_joke.return_value = 'one'
#     self.assertEqual(len_joke(), 3)

  # @patch('main.requests'):
  # def test_fail_len_joke(self, mock_requests):
  #   mock_resposne = MagicMock(status_code=403)
  #   mock_resposne.json.return_value = {
  #     'value' : {
  #       'joke' : 'hello world'
  #     }
  #   }

  #   mock_requests.get.return_value = mock_resposne

  #   self.assertEqual(len_joke(), 'No Jokes')


# if __name__ == '__main__':
#   unittest.main()
