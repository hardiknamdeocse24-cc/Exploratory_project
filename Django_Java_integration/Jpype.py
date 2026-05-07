# Only run this if you have a compiled Java class available
# This demonstrates how to call Bhaashik annotation tool methods

with bridge:
    try:
        # Example: call a Java NLP utility method
        # Replace 'YourClass' and 'yourMethod' with actual Bhaashik class names
        result = bridge.call_java_method(
            'BhaashikAnnotator',    # Java class name
            'annotate',             # method name
            ['घर जा रहा हूँ']       # args as list
        )
        print("Java method result:", result)
    except Exception as e:
        print("Java method call skipped (no compiled class found):", e)
        print("Export was successful — Java side can load embeddings from:", JAVA_EMB_PATH)
