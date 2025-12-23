import yaml
import os
import sys
import uuid
from typing import Dict, List, Any

def validate_rule(file_path: str) -> List[str]:
    errors = []
    try:
        with open(file_path, 'r') as f:
            rule = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"YAML parsing error: {e}"]
    except Exception as e:
        return [f"File error: {e}"]

    required_fields = ['title', 'id', 'status', 'description', 'author', 'date', 'logsource', 'detection', 'level']
    
    for field in required_fields:
        if field not in rule:
            errors.append(f"Missing required field: {field}")

    if 'id' in rule:
        try:
            uuid.UUID(str(rule['id']))
        except ValueError:
            errors.append("Invalid UUID format in 'id' field")

    if 'logsource' in rule:
        if not isinstance(rule['logsource'], dict):
            errors.append("'logsource' must be a dictionary")
        elif 'category' not in rule['logsource'] and 'product' not in rule['logsource']:
             errors.append("'logsource' must contain 'category' or 'product'")

    if 'detection' in rule:
        if 'condition' not in rule['detection']:
            errors.append("'detection' must contain 'condition'")

    return errors

def main():
    rules_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'rules', 'sigma')
    print(f"Scanning rules in: {rules_dir}")
    
    has_errors = False
    
    for root, _, files in os.walk(rules_dir):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                errors = validate_rule(file_path)
                
                if errors:
                    has_errors = True
                    print(f"\n❌ Invalid Rule: {file}")
                    for error in errors:
                        print(f"  - {error}")
                else:
                    print(f"✅ Valid Rule: {file}")

    if has_errors:
        sys.exit(1)
    else:
        print("\n✨ All rules passed validation!")
        sys.exit(0)

if __name__ == "__main__":
    main()
