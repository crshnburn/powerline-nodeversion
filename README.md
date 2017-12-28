# Powerline Nodeversion

A [Powerline](https://powerline.readthedocs.org/en/master/) segment for showing the current version of Node.js in the environment.

## Installation

Installation can be done with the pip command:

```sh
pip install git+https://github.com/crshnburn/powerline-nodeversion#egg=node_version
```

The following group needs adding to the colorscheme:

```json
{
    "groups": {
        "nodeversion": "information:regular"
    }
}
```

Add the segment to the segment configuration:

```json
{
    "function": "powerline_nodeversion.nodeversion"
}
```

## License

```text
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```