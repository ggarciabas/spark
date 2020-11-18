#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class StreamingListener:
    def __init__(self) -> None: ...
    def onStreamingStarted(self, streamingStarted: Any) -> None: ...
    def onReceiverStarted(self, receiverStarted: Any) -> None: ...
    def onReceiverError(self, receiverError: Any) -> None: ...
    def onReceiverStopped(self, receiverStopped: Any) -> None: ...
    def onBatchSubmitted(self, batchSubmitted: Any) -> None: ...
    def onBatchStarted(self, batchStarted: Any) -> None: ...
    def onBatchCompleted(self, batchCompleted: Any) -> None: ...
    def onOutputOperationStarted(self, outputOperationStarted: Any) -> None: ...
    def onOutputOperationCompleted(self, outputOperationCompleted: Any) -> None: ...
    class Java:
        implements: Any = ...