import requests
from typing import Optional, Dict, Any, List, Union
import os
from pathlib import Path
try:
    from dotenv import load_dotenv
    # Load .env from the project root (parent of 'scripts' directory)
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    # Handle case where python-dotenv is not installed
    pass

class ZentaoClient:
    """
    A client for the ZenTao RESTful API v1.0.
    Based on the official documentation.
    """
    def __init__(self, base_url: str):
        """
        Initialize the client.
        :param base_url: The base URL of the ZenTao installation (e.g. 'http://pms.zentao.net/api.php/v1')
        """
        self.base_url = base_url.rstrip('/')
        self.token = None
        self.headers = {
            'Content-Type': 'application/json'
        }

    def authenticate(self, account: str, password: str) -> str:
        """
        Get an authentication token.
        :param account: Username
        :param password: Password
        :return: The authentication token
        """
        url = f"{self.base_url}/tokens"
        payload = {
            "account": account,
            "password": password
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.token = data.get('token')
        if self.token:
            self.headers['Token'] = self.token
        return self.token

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, json_data: Optional[Dict] = None, files: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        if files:
            # When sending files, let requests handle Content-Type (multipart/form-data)
            headers = self.headers.copy()
            headers.pop('Content-Type', None)
            # For multipart, other data usually goes into 'data', not 'json'
            response = requests.post(url, headers=headers, data=json_data, files=files)
        else:
            response = requests.post(url, headers=self.headers, json=json_data)
        response.raise_for_status()
        return response.json()

    def _put(self, endpoint: str, json_data: Dict) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=self.headers, json=json_data)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str) -> Any:
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    # --- User & Dept APIs ---
    def get_users(self, page: int = 1, limit: int = 20) -> List[Dict]:
        return self._get('/users', params={'page': page, 'limit': limit})
        
    def create_user(self, user_data: Dict) -> Dict:
        return self._post('/users', user_data)
        
    def get_departments(self) -> List[Dict]:
        return self._get('/departments')

    # --- Program (Project Set) APIs ---
    def get_programs(self, status: str = 'all', limit: int = 20, page: int = 1) -> List[Dict]:
        return self._get('/programs', params={'status': status, 'limit': limit, 'page': page})

    def create_program(self, program_data: Dict) -> Dict:
        return self._post('/programs', program_data)

    def get_program_details(self, program_id: int) -> Dict:
        return self._get(f'/programs/{program_id}')

    def update_program(self, program_id: int, program_data: Dict) -> Dict:
        return self._put(f'/programs/{program_id}', program_data)

    def delete_program(self, program_id: int) -> Dict:
        return self._delete(f'/programs/{program_id}')

    # --- Product APIs ---
    def get_products(self) -> List[Dict]:
        return self._get('/products')

    def get_product_details(self, product_id: int) -> Dict:
        return self._get(f'/products/{product_id}')
        
    def get_plans(self, product_id: int) -> List[Dict]:
        return self._get(f'/products/{product_id}/plans')
        
    def create_plan(self, product_id: int, plan_data: Dict) -> Dict:
        return self._post(f'/products/{product_id}/plans', plan_data)
        
    def get_releases(self, product_id: int) -> List[Dict]:
        return self._get(f'/products/{product_id}/releases')

    # --- Project & Execution APIs ---
    def get_projects(self) -> List[Dict]:
        return self._get('/projects')
        
    def get_project_details(self, project_id: int) -> Dict:
        return self._get(f'/projects/{project_id}')

    def get_executions(self, project_id: int) -> List[Dict]:
        return self._get(f'/projects/{project_id}/executions')

    # --- Bug APIs ---
    def get_product_bugs(self, product_id: int) -> List[Dict]:
        return self._get(f'/products/{product_id}/bugs')

    def create_bug(self, product_id: int, bug_data: Dict) -> Dict:
        return self._post(f'/products/{product_id}/bugs', bug_data)

    def resolve_bug(self, bug_id: int, params: Dict) -> Dict:
        return self._post(f'/bugs/{bug_id}/resolve', params)
        
    def get_bug_details(self, bug_id: int) -> Dict:
        return self._get(f'/bugs/{bug_id}')

    # --- Task APIs ---
    def get_execution_tasks(self, execution_id: int) -> List[Dict]:
        return self._get(f'/executions/{execution_id}/tasks')

    def create_task(self, execution_id: int, task_data: Dict) -> Dict:
        return self._post(f'/executions/{execution_id}/tasks', task_data)
        
    def get_task_details(self, task_id: int) -> Dict:
        return self._get(f'/tasks/{task_id}')

    # --- Story (Requirement) APIs ---
    def get_product_stories(self, product_id: int, status: str = 'active') -> List[Dict]:
        return self._get(f'/products/{product_id}/stories', params={'status': status})

    def create_story(self, story_data: Dict) -> Dict:
        return self._post('/stories', story_data)

    # --- Test Case APIs ---
    def get_product_cases(self, product_id: int) -> List[Dict]:
        return self._get(f'/products/{product_id}/cases')
        
    def create_case(self, case_data: Dict) -> Dict:
        return self._post('/cases', case_data)
        
    # --- Feedback & Ticket APIs ---
    def get_feedbacks(self) -> List[Dict]:
        return self._get('/feedbacks')
        
    def create_feedback(self, feedback_data: Dict) -> Dict:
        return self._post('/feedbacks', feedback_data)
        
    def get_tickets(self) -> List[Dict]:
        return self._get('/tickets')

    # --- Doc APIs ---
    def get_doc_libs(self, type: str = 'product', object_id: int = 0) -> List[Dict]:
        """
        Get document libraries.
        :param type: 'product', 'project', etc.
        :param object_id: ID of the product/project
        """
        return self._get('/doclibs', params={'type': type, 'objectID': object_id})

    def get_docs(self, lib_id: int, limit: int = 20, page: int = 1) -> List[Dict]:
        return self._get(f'/doclibs/{lib_id}/docs', params={'limit': limit, 'page': page})

    def get_doc_details(self, doc_id: int) -> Dict:
        return self._get(f'/docs/{doc_id}')

    def create_doc(self, doc_data: Dict) -> Dict:
        return self._post('/docs', doc_data)

    def update_doc(self, doc_id: int, doc_data: Dict) -> Dict:
        return self._put(f'/docs/{doc_id}', doc_data)

    def delete_doc(self, doc_id: int) -> Dict:
        return self._delete(f'/docs/{doc_id}')

    # --- File APIs ---
    def upload_file(self, file_path: str, object_type: str = None, object_id: int = 0) -> Dict:
        """
        Upload a file.
        :param file_path: Local path to the file
        :param object_type: Type of object to attach to (e.g., 'bug')
        :param object_id: ID of the object
        """
        with open(file_path, 'rb') as f:
            files = {'files': f} # ZenTao might expect 'files' or 'file'
            # Some versions use /files, some might attach directly. Using generic /files if available or assume 'files' param name.
            # Checking docs (implicit): POST /files
            params = {}
            if object_type: params['objectType'] = object_type
            if object_id: params['objectID'] = object_id
            return self._post('/files', json_data=params, files=files)

    def get_file(self, file_id: int) -> Dict:
        return self._get(f'/files/{file_id}')

    def delete_file(self, file_id: int) -> Dict:
        return self._delete(f'/files/{file_id}')

    # --- Generic/Action APIs ---
    def get_object_actions(self, object_type: str, object_id: int) -> List[Dict]:
        """
        Get action history for an object.
        Note: The endpoint structure depends on API version specifics, 
        often /actions?objectType=bug&objectID=1 or similar. 
        If specific endpoints exist (like /bugs/1/actions), prefer those.
        Here we assume a generic lookup or return NotImplemented if not standard.
        Based on scrape, maybe not explicitly generic.
        Let's try to map common ones if possible, or use a generic pattern if ZenTao supports it.
        Without explicit generic endpoint documentation, we might skip or rely on detail views.
        """
        # Placeholder for future expansion
        pass

    # --- Additional Test APIs ---
    def get_test_suites(self, product_id: int) -> List[Dict]:
         return self._get(f'/products/{product_id}/suites')
         
    def get_test_reports(self, project_id: int) -> List[Dict]:
         return self._get(f'/projects/{project_id}/testreports')

# Helper function to easily call from agent
def get_client(base_url: str = None, account: str = None, password: str = None) -> ZentaoClient:
    # Use provided arguments, or fall back to environment variables, or fall back to defaults
    if not base_url:
        base_url = os.getenv('ZENTAO_BASE_URL', '')
    if not account:
        account = os.getenv('ZENTAO_ACCOUNT', '')
    if not password:
        password = os.getenv('ZENTAO_PASSWORD', '')
        
    client = ZentaoClient(base_url)
    if account and password:
        client.authenticate(account, password)
    return client
