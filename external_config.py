"""
This module stores configuration for external system connections.
It's structured to allow easy manual adjustments post-deployment.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection configurations
ORACLE_DB_CONFIGS = {
    "oracle_db1": {
        "host": os.environ.get("ORACLE_DB1_HOST", ""),
        "port": os.environ.get("ORACLE_DB1_PORT", "1521"),
        "service_name": os.environ.get("ORACLE_DB1_SERVICE", ""),
        "username": os.environ.get("ORACLE_DB1_USERNAME", ""),
        "password": os.environ.get("ORACLE_DB1_PASSWORD", ""),
    },
    "oracle_db2": {
        "host": os.environ.get("ORACLE_DB2_HOST", ""),
        "port": os.environ.get("ORACLE_DB2_PORT", "1521"),
        "service_name": os.environ.get("ORACLE_DB2_SERVICE", ""),
        "username": os.environ.get("ORACLE_DB2_USERNAME", ""),
        "password": os.environ.get("ORACLE_DB2_PASSWORD", ""),
    }
}

SYBASE_DB_CONFIGS = {
    "sybase_db1": {
        "host": os.environ.get("SYBASE_DB1_HOST", ""),
        "port": os.environ.get("SYBASE_DB1_PORT", "5000"),
        "database": os.environ.get("SYBASE_DB1_DATABASE", ""),
        "username": os.environ.get("SYBASE_DB1_USERNAME", ""),
        "password": os.environ.get("SYBASE_DB1_PASSWORD", ""),
    },
    "sybase_db2": {
        "host": os.environ.get("SYBASE_DB2_HOST", ""),
        "port": os.environ.get("SYBASE_DB2_PORT", "5000"),
        "database": os.environ.get("SYBASE_DB2_DATABASE", ""),
        "username": os.environ.get("SYBASE_DB2_USERNAME", ""),
        "password": os.environ.get("SYBASE_DB2_PASSWORD", ""),
    }
}

# SSH connection configurations for Linux hosts
SSH_CONFIGS = {
    "linux_host1": {
        "hostname": os.environ.get("SSH_HOST1", ""),
        "port": os.environ.get("SSH_PORT1", "22"),
        "username": os.environ.get("SSH_USERNAME1", ""),
        "password": os.environ.get("SSH_PASSWORD1", ""),
        "key_filename": os.environ.get("SSH_KEY1", ""),
    },
    "linux_host2": {
        "hostname": os.environ.get("SSH_HOST2", ""),
        "port": os.environ.get("SSH_PORT2", "22"),
        "username": os.environ.get("SSH_USERNAME2", ""),
        "password": os.environ.get("SSH_PASSWORD2", ""),
        "key_filename": os.environ.get("SSH_KEY2", ""),
    }
}

# Example functions for connection
def get_oracle_connection_string(config_name):
    """
    Get Oracle connection string from configuration.
    
    Args:
        config_name (str): The name of the configuration in ORACLE_DB_CONFIGS
        
    Returns:
        str: Connection string for Oracle database
    """
    config = ORACLE_DB_CONFIGS.get(config_name)
    if not config:
        return None
    
    return f"oracle+cx_oracle://{config['username']}:{config['password']}@" \
           f"{config['host']}:{config['port']}/{config['service_name']}"

def get_sybase_connection_string(config_name):
    """
    Get Sybase connection string from configuration.
    
    Args:
        config_name (str): The name of the configuration in SYBASE_DB_CONFIGS
        
    Returns:
        str: Connection string for Sybase database
    """
    config = SYBASE_DB_CONFIGS.get(config_name)
    if not config:
        return None
    
    return f"sybase+pyodbc://{config['username']}:{config['password']}@" \
           f"{config['host']}:{config['port']}/{config['database']}"

def get_ssh_config(config_name):
    """
    Get SSH configuration.
    
    Args:
        config_name (str): The name of the configuration in SSH_CONFIGS
        
    Returns:
        dict: SSH configuration dictionary
    """
    return SSH_CONFIGS.get(config_name)
