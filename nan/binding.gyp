{
  "targets": [
    {
      "target_name": "nan",
      "sources": [ "index.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
